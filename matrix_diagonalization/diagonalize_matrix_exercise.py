import numpy as np

a=np.array([[0.7,0.2]
           ,[0.3,0.8]])

eigenvalue,eigenvector=np.linalg.eig(a)

print(eigenvalue) 
print(eigenvector)
# [0.5 1. ]
# [[-0.70710678 -0.5547002 ]
#  [ 0.70710678 -0.83205029]]

#test for the answer
print(a@eigenvector@np.linalg.pinv(eigenvector))
# [[0.7 0.2]
#  [0.3 0.8]]