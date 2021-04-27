import numpy as np
import matplotlib.pyplot as plt

def coefficient_matrix(N):
    A=np.zeros((N,N))
    for i in range(0,N):
        if i==0:
            A[i,0]=1
        elif i==N-1:
            A[i,-1]=1
        else:
            A[i,i]=-2
            A[i,i+1]=1
            A[i,i-1]=1
    return A


def rho(N):
    rho=np.zeros((N))
    rho[int(N/2)]=1
    return rho


#parameters:
#grid number in x direction
N=11
L=1
h=L/(N-1)
x=h*np.arange(0,N)


A=coefficient_matrix(N)
print(A)
rho=rho(N)
V=-h*np.linalg.inv(A)@rho

plt.plot(x,V)
plt.xlabel('x(L)')
plt.ylabel('V ($\sigma/\epsilon_0 \epsilon_b$)')
plt.show()