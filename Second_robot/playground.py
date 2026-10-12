import numpy as np
arr = np.array([[0,1,2,3,4,5,6,8,9],
               [0,1,2,3,4,5,6,8,9],
               [0,1,2,3,4,5,6,8,9]])
arr[:, 3:6] = [
    [9, 9, 9],
    [9, 9, 9],
    [9, 9, 9],
]
print(arr)
print(len(arr))