from pogema import pogema_v0, GridConfig
import numpy as np
import pandas as pd


# ============================================================
# LEVEL 2 FACTORY
# ============================================================

FACTORY_MAP = """
###############
#.............#
#.###.###.###.#
#...#.....#...#
#...#.###.#...#
#.............#
#.###.....###.#
#.....###.....#
#.###.....###.#
#.............#
#...#.###.#...#
#...#.....#...#
#.###.###.###.#
#.............#
###############
"""


# En agent.
#
# Den börjar på [1, 1].
#
# När den når ett mål får den nästa mål i listan.
# När sista målet är klart börjar POGEMA om från början
# i målsekvensen.
LEVEL_2_GOALS = [
    [
        [1, 13],
        [5, 7],
        [13, 13],
        [13, 1],
        [9, 7],
        [3, 3],
        [11, 11],
        [7, 5],
        [1, 7],
        [13, 7],
    ]
]


class gym:

    def __init__(self):

        # ----------------------------------------------------
        # Environment configuration
        # ----------------------------------------------------

        self.grid_config = GridConfig(

            # Samma fabrik hela tiden
            map=FACTORY_MAP,

            # En robot
            num_agents=1,

            # Fast startposition
            agents_xy=[
                [1, 1]
            ],

            # Flera mål efter varandra
            targets_xy=LEVEL_2_GOALS,

            # När ett mål nås:
            # ge roboten nästa mål.
            on_target="restart",

            # Begränsad syn
            #
            # radius 5:
            #
            # 5 + robot + 5
            # = 11 x 11 observation
            obs_radius=5,

            # Vi vill INTE ge algoritmen hela kartan.
            #
            # POMAPF ger:
            # - lokal obstacle observation
            # - lokal agent observation
            # - position
            # - target position
            observation_type="POMAPF",

            # Level 2 ska kunna bestå av många orders
            max_episode_steps=5000,

            # Reproducerbart test
            seed=42
        )

        # ----------------------------------------------------
        # Create environment
        # ----------------------------------------------------

        self.env = pogema_v0(
            grid_config=self.grid_config
        )

        self.obs, self.info = self.env.reset()

        self.reward = [0.0]
        self.terminated = [False]
        self.truncated = [False]

        # Hur många mål/orders roboten har klarat
        self.orders_completed = 0

        # Storleken på LOCAL observation
        self.obs_rows = self.grid_config.obs_radius * 2 + 1
        self.obs_cols = self.grid_config.obs_radius * 2 + 1

        # Storleken på den riktiga fabriken.
        #
        # OBS:
        # Detta berättar endast storleken.
        # Det ger INTE algoritmen obstacle-kartan.
        factory_lines = [
            line
            for line in FACTORY_MAP.strip().splitlines()
            if line
        ]

        self.factory_rows = len(factory_lines)
        self.factory_cols = len(factory_lines[0])


    # ========================================================
    # BASIC ENVIRONMENT METHODS
    # ========================================================

    def render(self):
        """
        Render the real environment.

        This is mainly for us humans.
        The pathfinding algorithm should not use this
        as knowledge about the map.
        """

        self.env.render()


    def step(self, actions):
        """
        Execute one action.

        Actions:
            0 = wait
            1 = up
            2 = down
            3 = left
            4 = right
        """

        (
            self.obs,
            self.reward,
            self.terminated,
            self.truncated,
            self.info
        ) = self.env.step(actions)

        # In lifelong mode terminated does NOT mean
        # "order completed".
        #
        # Reward = 1 means the robot reached its goal
        # during this step.
        if self.reward[0] > 0:
            self.orders_completed += 1

        return (
            self.obs,
            self.reward,
            self.terminated,
            self.truncated,
            self.info
        )


    # ========================================================
    # LOCAL SENSOR DATA
    # ========================================================

    def get_local_observation(self):
        """
        Return ONLY what the robot can currently see.

        Returns:
            obstacles:
                11x11 array

            agents:
                11x11 array
        """

        robot_obs = self.obs[0]

        obstacles = robot_obs["obstacles"].copy()
        agents = robot_obs["agents"].copy()

        return obstacles, agents


    def get_local_obstacle_df(self):
        """
        Convenience function.

        IMPORTANT:
        row/col in this DataFrame are LOCAL coordinates
        inside the 11x11 observation.

        They are NOT factory coordinates.
        """

        obstacles, _ = self.get_local_observation()

        df_obstacles = pd.DataFrame(
            np.argwhere(obstacles == 1),
            columns=["row", "col"]
        )

        return df_obstacles


    # ========================================================
    # POSITION / TARGET
    # ========================================================

    def get_current_pos(self):
        """
        Robot position in POGEMA's coordinate frame.
        """

        xy = self.obs[0]["xy"]

        return (
            int(xy[0]),
            int(xy[1])
        )


    def get_goal_pos(self):
        """
        Current target position in the same coordinate frame
        as get_current_pos().
        """

        target_xy = self.obs[0]["target_xy"]

        return (
            int(target_xy[0]),
            int(target_xy[1])
        )


    def get_goal_and_current_pos(self):
        """
        Convenience method.
        """

        current_pos = self.get_current_pos()
        goal_pos = self.get_goal_pos()

        return current_pos, goal_pos


    # ========================================================
    # LEVEL / ORDER STATUS
    # ========================================================

    def goal_reached_this_step(self):
        """
        True only on the step where the current goal
        was reached.
        """

        return self.reward[0] > 0


    def get_orders_completed(self):
        return self.orders_completed


    def is_truncated(self):
        """
        True if the complete Level 2 run hit the
        maximum episode length.
        """

        return self.truncated[0]


    # ========================================================
    # DEBUG / INFORMATION
    # ========================================================

    def get_observation_shape(self):
        return (
            self.obs_rows,
            self.obs_cols
        )


    def get_factory_shape(self):
        return (
            self.factory_rows,
            self.factory_cols
        )


    def print_status(self):

        current_pos = self.get_current_pos()
        goal_pos = self.get_goal_pos()

        print(
            f"Position: {current_pos} | "
            f"Goal: {goal_pos} | "
            f"Orders completed: {self.orders_completed}"
        )


    # ========================================================
    # FULL RESET
    # ========================================================

    def reset(self):
        """
        Restart the COMPLETE Level 2 scenario.

        This sends the robot back to the beginning
        and restarts the target sequence.

        This should NOT be called between normal orders.
        """

        self.obs, self.info = self.env.reset()

        self.reward = [0.0]
        self.terminated = [False]
        self.truncated = [False]

        self.orders_completed = 0

        return self.obs, self.info