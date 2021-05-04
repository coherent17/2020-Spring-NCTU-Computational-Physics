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

b=np.array([[0,-1j]
           ,[1j,0]])

eigenvalue,eigenvector=np.linalg.eig(b)
print(eigenvalue) 
print(eigenvector)
# [ 1.+0.j -1.+0.j]
# [[-0.        -0.70710678j  0.70710678+0.j        ]
#  [ 0.70710678+0.j          0.        -0.70710678j]]

print(b@eigenvector@np.linalg.pinv(eigenvector))
# [[-3.33066907e-16-3.92523115e-17j -3.92523115e-17-1.00000000e+00j]
#  [-3.92523115e-17+1.00000000e+00j -2.22044605e-16+3.92523115e-17j]]