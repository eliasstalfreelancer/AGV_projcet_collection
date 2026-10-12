from gym import gym
from path_finding import get_goal_path, Node

def main():
    points = 0
    
    for i in range(100):
        env = gym()
        env.render()
        current_pos, goal_pos = env.get_goal_and_current_pos()
        #print(env.get_current_environment_df())
        #print("Current Position:", current_pos)
        #print("Goal Position:", goal_pos)
        path = get_goal_path(current_pos=current_pos, goal_pos=goal_pos, env=env)
        #[1](up), [2](down), [3](left), [4](right)
        
        path.pop(0)  # Remove the first element, which is the current position
        #print("Path to goal:", path)
        #print(obsticals := env.df_obstacles)
        for step in path:
            #print("Step:", step)
            #print([step])
            env.step([step])
            #env.render()
        if env.terminated[0]:
            print(i, "Goal reached!")
            points += 1
    print(f"Points: {points}/100")
if __name__ == "__main__":
    main()
