"""
TODO: create a 2d array of the obs 


"""
import numpy as np
import matplotlib.pyplot as plt
import os



class map:
    def __init__(self,env) -> None:
        self.curent_map = env.get_local_observation()[0]
        self.visited = {env.get_current_pos()}
        self.env = env
        self.past_pos_set = env.get_current_pos()
        self.offset = [5,5]
    def show_map(self):


        plt.figure(figsize=(10, 10))

        plt.imshow(
            self.curent_map,
            interpolation="nearest"
        )

        plt.xticks(range(self.curent_map.shape[1]))
        plt.yticks(range(self.curent_map.shape[0]))

        plt.grid(True)

        plt.title(
            f"Internal map: "
            f"{self.curent_map.shape[0]}x"
            f"{self.curent_map.shape[1]}"
        )
        fig_manager = plt.get_current_fig_manager()

        fig_manager.window.state('zoomed')
        plt.show()

    def up(self,obs):
        self.step = [1]
        obs = self.fill_arr(obs[0])
        self.curent_map = np.vstack((obs,self.curent_map))
        return self.curent_map

    def down(self,obs):
        self.step = [2]
        print("colum_arr: ",len(obs[-1]))
        obsfill = self.fill_arr(obs[-1])
        print("colum_arrfill: ",len(obsfill))
        self.curent_map = np.vstack((self.curent_map,obsfill))
        return self.curent_map

    def right(self,obs):

        self.step = [4]
        
        colum = []

        for i in range(len(obs)):
            colum.append(obs[i][-1])
        
        colum_arr = np.array(colum)
       
        colum_arr_fill = self.fill_arr(colum_arr)
        
        colum_arr_reshape = colum_arr_fill.reshape(len(colum_arr_fill),1)

        
        self.curent_map = np.hstack((self.curent_map,colum_arr_reshape))
        
        return self.curent_map



    def left(self,obs):
        self.step = [3]
                
        colum = []

        for i in range(len(obs)):
            colum.append(obs[i][0])
        
        colum_arr = np.array(colum)
        
        colum_arr_fill = self.fill_arr(colum_arr)
        
        colum_arr_reshape = colum_arr_fill.reshape(len(colum_arr_fill),1)

        
        self.curent_map = np.hstack((colum_arr_reshape,self.curent_map))
        
        return self.curent_map
    
    def flash(self,new_obs,env):
        curent_map = self.curent_map
        x,y = env.get_current_pos()
        x1,y1 = self.offset
        obs_shape = new_obs.shape
        render_index = [x+x1-obs_shape[0],x+x1-obs_shape[0]]
        old_obs = curent_map

        if new_obs != old_obs:
            curent_map[:,render_index[0],render_index[1]]
        self.curent_map = curent_map
            
    def fill_arr(self, arr):

        step = self.step[0]
        x, y = self.curent_map.shape
        
        
        if step in [1,2] : 

            if y > len(arr):

                while y > len(arr):

                    if step == 1:
                        arr = np.append(arr,[-1])

                    if step == 2:
                        arr = np.insert(arr,0,[-1])
            
        
        elif step in [3,4]: 

            if x > len(arr):
                
                while x > len(arr):
                    len(arr)
                    if step == 3:
                        arr = np.insert(arr,0,[-1])

                    if step == 4:
                        arr = np.insert(arr,0,[-1])
        
                    

        return arr
    

    def insert_self(self,obs,offset,env):
        past_pos_set = self.past_pos_set
        curent_pos= env.get_current_pos()
       
        past_pos = past_pos_set
        x1,y1 = (past_pos[0] + offset[0], past_pos[1] + offset[1])
        obs[x1][y1] = 0

        x,y = (curent_pos[0] + offset[0], curent_pos[1] + offset[1])
        print("xxxxxx")
        print(x)
        print(y)
        print("xxxxxx")
        obs[x][y] = 3
        print(3 in obs)
        return obs


    def update_offset(self,offset):
        
        y,x = 1,0
        step = self.step
        print(step)
        if step == [1] :
            offset[x] += 1
        if step == [2] and offset[x] < 5:
            offset[x] -= 1

        
        if step == [4]:
            offset[y] += 1
        if step == [3] and offset[y] < 5:
            offset[y] -= 1
        
        return offset

    
    def update_map(self,local_obs,step,env):
        self.step = step
        if env.get_current_pos() not in self.visited:
            self.visited.add(env.get_current_pos())
            
            if step == [1]:
                local_obs =  self.up(local_obs)

            elif step == [2]:
                local_obs = self.down(local_obs)

            elif step == [3]:
                local_obs = self.left(local_obs)

            elif step == [4]:
                local_obs = self.right(local_obs)
        self.offset = self.update_offset(self.offset)
        print(self.offset)
        local_obs = self.insert_self(local_obs,self.offset,env)
        self.past_pos_set = env.get_current_pos()
        return local_obs
        