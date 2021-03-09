import numpy as np

A=np.array([[2,5,5]
           ,[4,8,5]
           ,[1,1,1]])

B=np.array([12,17,3])
x=np.linalg.solve(A,B)
print(x)
# [1. 1. 1.]

C=np.array([[1,1]
          ,[2,2]])
D=np.array([2,4])
x=np.linalg.solve(C,D)
print(x)