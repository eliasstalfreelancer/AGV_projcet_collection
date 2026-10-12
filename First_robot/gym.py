from pogema import pogema_v0, GridConfig
import pandas as pd
import numpy as np


class gym:

    def __init__(self):
        self.grid_config = GridConfig(
            num_agents=1,
            size=10,
            density=0.25,
            
            obs_radius=10,
            max_episode_steps=200
        )

        self.env = pogema_v0(
            grid_config=self.grid_config,
            observation_type="MAPF"
        )

        self.obs, self.info = self.env.reset()

        self.reward = 0
        self.terminated = False
        self.truncated = False

        self.df_obstacles = None
        self.df_agents = None
        self.df_goals = None

        self.obs_rows = None
        self.obs_cols = None


    def render(self):
        self.env.render()


    def step(self, actions):
        (
            self.obs,
            self.reward,
            self.terminated,
            self.truncated,
            self.info
        ) = self.env.step(actions)


    def get_current_environment_df(self):

        robot_obs = self.obs[0]

        obstacles = robot_obs[0]
        agents = robot_obs[1]
        goals = robot_obs[2]

        # Storleken på ROBOTENS LOKALA OBSERVATION
        self.obs_rows, self.obs_cols = obstacles.shape

        self.df_obstacles = pd.DataFrame(
            np.argwhere(obstacles == 1),
            columns=["row", "col"]
        )

        self.df_agents = pd.DataFrame(
            np.argwhere(agents == 1),
            columns=["row", "col"]
        )

        self.df_goals = pd.DataFrame(
            np.argwhere(goals == 1),
            columns=["row", "col"]
        )

        return (
            self.df_obstacles,
            self.df_agents,
            self.df_goals
        )


    def get_goal_and_current_pos(self):

        (
            df_obstacles,
            df_agents,
            df_goals
        ) = self.get_current_environment_df()

        current_pos = df_agents.iloc[0]
        goal_pos = df_goals.iloc[0]

        return current_pos, goal_pos