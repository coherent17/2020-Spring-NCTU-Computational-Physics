import numpy as np

A=np.array([[0.7,0.2]
          ,[0.3,0.8]])

for i in range(3):
    A=np.matmul(A,A)

print(A)