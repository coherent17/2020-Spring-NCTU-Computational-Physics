import numpy as np

a=np.array([[1,1,0,0,0]
           ,[1,1,1,0,0]
           ,[0,1,1,1,0]
           ,[0,0,1,1,1]
           ,[0,0,0,1,1]])

eigenvalue,eigenvector=np.linalg.eig(a)
print(eigenvalue)
print(eigenvector)
sort_ind=np.argsort(eigenvalue)
eigenvalue=eigenvalue[sort_ind]
eigenvector=eigenvector[:,sort_ind]
print('after sorting')
print(eigenvalue)
print(eigenvector)
