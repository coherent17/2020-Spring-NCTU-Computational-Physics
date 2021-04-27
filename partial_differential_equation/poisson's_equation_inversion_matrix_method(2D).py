import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt

def coefficient_matrix(N):
    A=np.zeros((N**2,N**2))
    for i in range(0,N**2):
        #boundary condition:V=0
        if i<N:A[i,i]=1           #bottom
        elif i>=N**2-(N):A[i,i]=1 #top
        elif i%N==0:A[i,i]=1      #left
        elif (i+1)%N==0:A[i,i]=1  #right

        #FDM
        else:
            A[i,i]=-4  #target
            A[i,i-N]=1 #bottom
            A[i,i+N]=1 #up
            A[i,i+1]=1 #right
            A[i,i-1]=1 #left
    return A

def rho(N):
    rho=np.zeros((N))
    rho[int(N/2)]=1
    return rho

N=51
A=coefficient_matrix(N)
rho=rho(N)
print(rho)
# V=np.linalg.inv(A)@rho
# print(V)


