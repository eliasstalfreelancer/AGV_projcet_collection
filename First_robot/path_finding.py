import numpy as np
import pandas as pd

class Node:

    def __init__(
        self,
        position,
        parent=None,
        obstacles=None,
        action=None,
        rows=None,
        cols=None
    ):
        self.position = position
        self.parent = parent
        self.children = []
        self.action = action
        self.obstacles = obstacles

        self.rows = rows
        self.cols = cols

    def validate_position(self, position):

        row, col = position

        # Utanför observationen
        if row < 0 or row >= self.rows:
            return False

        if col < 0 or col >= self.cols:
            return False

        # Hinder
        is_obstacle = (
            (self.obstacles["row"] == row)
            &
            (self.obstacles["col"] == col)
        ).any()

        if is_obstacle:
            return False

        return True

    def add_child(self, child):
        self.children.append(child)

   
        
def get_path(node):
        path = []

        while node is not None:
            path.append(node.action)
            node = node.parent

        return path[::-1]
    
def get_goal_path(current_pos, goal_pos, env): 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    
    og_pratns = []
    partents = []
    
    root = Node(
    position=(
        current_pos["row"],
        current_pos["col"]
    ),
    parent=None,
    obstacles=env.df_obstacles,
    rows=env.obs_rows,
    cols=env.obs_cols
)
    parents = [root]

    visited = {root.position}
    
    while parents:

        current_node = parents.pop(0)

        #print("\nExploring:", current_node.position)
        #print("Nodes waiting:", len(parents))

        valid_children = 0

        for direction in directions:

            new_position = (
                current_node.position[0] + direction[0],
                current_node.position[1] + direction[1]
            )

            if new_position in visited:
                #print(new_position, "-> VISITED")
                continue

            if not current_node.validate_position(new_position):
                
                #print(new_position, "-> OBSTACLE")
                continue

            #print(new_position, "-> VALID")
            valid_children += 1

            
            child_node = Node(
                position=new_position,
                parent=current_node,
                action=directions.index(direction) + 1,
                obstacles=env.df_obstacles,
                rows=env.obs_rows,
                cols=env.obs_cols
            )

            current_node.add_child(child_node)

            visited.add(new_position)
            parents.append(child_node)

            if new_position == (
                goal_pos["row"],
                goal_pos["col"]
            ):
                

                return get_path(child_node)
    print("\n========== BFS FAILED ==========")
    print("Start:", root.position)
    print("Goal:", (
        int(goal_pos["row"]),
        int(goal_pos["col"])
    ))
    print("Visited:", len(visited))
    print("Goal visited:", (
        int(goal_pos["row"]),
        int(goal_pos["col"])
    ) in visited)
    print("Remaining parents:", len(parents))
    print("================================")

    return None
        