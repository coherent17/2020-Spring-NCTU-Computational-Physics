import numpy as np

A=np.array([[1,-1,1]
           ,[-1,1,-1]
           ,[4,2,0]
           ,[0,2,5]])



B=np.array([[0]
           ,[0]
           ,[8]
           ,[9]])

C=np.c_[A,B]