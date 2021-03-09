import numpy as np

A=np.array([[2,1]
          ,[2,1.001]])

B=np.array([3,0])

x=np.linalg.solve(A,B)
print(x)

A=np.array([[2,1]
          ,[2,1.0011]])

B=np.array([3,0])
x=np.linalg.solve(A,B)
print(x)

