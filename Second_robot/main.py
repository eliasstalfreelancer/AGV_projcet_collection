from gym import gym
import numpy as np
from internal_map import map

if __name__ == "__main__":
    env = gym()
    env.reset()
    env.render()

    #1,2,3,4 up, down, left,right
    
    curent_map = env.get_local_observation()[0]
    print("curent_map:", curent_map.shape)
    step = [0]
    class_map = map(env)
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]
    curent_map = class_map.update_map(obs,step,env)
    class_map.show_map()
    
    step = [4]
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]
    curent_map = class_map.update_map(obs,step,env)
    
    print("curent_map:",curent_map.shape)
    class_map.show_map()
    
    step = [3]
    
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]

    curent_map = class_map.update_map(obs,step,env)

    class_map.show_map()
    step = [2]
        
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]

    curent_map = class_map.update_map(obs,step,env)

    class_map.show_map()
    
    step = [2]
            
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]

    curent_map = class_map.update_map(obs,step,env)

    class_map.show_map()
    print("curent_map:",curent_map.shape)
    step = [4]
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]
   
    curent_map = class_map.update_map(obs,step,env)
    class_map.show_map()
    
    print("curent_map:",curent_map.shape)


    step = [4]
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]

    curent_map = class_map.update_map(obs,step,env)
    class_map.show_map()

    print("curent_map:",curent_map.shape)

    
    step = [2]
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]

    curent_map = class_map.update_map(obs,step,env)
    class_map.show_map()
    


    step = [3]
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]

    curent_map = class_map.update_map(obs,step,env)
    class_map.show_map()
    step = [3]
    obs, reward, terminated, truncated, info = env.step(actions=step)
    obs = obs[0]["obstacles"]

    curent_map = class_map.update_map(obs,step,env)
    class_map.show_map()

    
    
    
    

    



    
