import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt

def coefficient_matrix(N):
    A=np.identity(N**2)
    #mid row (midpoint of the matrix:(int((N**2+1)/2)-1,int((N**2+1)/2)-1))
    #because the index begin from the index 0, thus minus 1
    A[int((N**2+1)/2)-1,int((N**2+1)/2)-1-3]=1
    A[int((N**2+1)/2)-1,int((N**2+1)/2)-1-1]=1
    A[int((N**2+1)/2)-1,int((N**2+1)/2)-1]=-4
    A[int((N**2+1)/2)-1,int((N**2+1)/2)-1+1]=1
    A[int((N**2+1)/2)-1,int((N**2+1)/2)-1+3]=1
    return A

def rho(N):
    rho=np.zeros((N**2))
    rho[int((N**2+1)/2)-1]=1
    return rho

N=5
A=coefficient_matrix(N)
print(A)
rho=rho(N)
V=-1*np.linalg.pinv(A)@rho