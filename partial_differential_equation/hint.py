import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt

def Building_mat(n_x,n_y):
    A = np.zeros((n_x**2,n_y**2),dtype=float)

    for i in range(0, n_x*n_y):
            if (i < n_x): # bottom
                A[i,i] = 1
            elif (i % n_x==0): # left
                A[i,i] = 1
            elif (i % n_x==n_x-1): # right
                A[i,i] = 1
            elif (i >= A.shape[0]-n_x): # top
                A[i,i] = 1
            else:
                A[i,i-n_x] = 1
                A[i,i-1] = 1
                A[i,i] = -4 
                A[i,i+1] = 1 
                A[i,i+n_x] = 1
    return A



n = 5 #number of grids
L = 1
h = L/(n-1)
x = np.linspace(0,L,n)
y = np.linspace(0,L,n)

rho = np.zeros((n**2,1),dtype=float)
lam = 1
rho[int((n**2-1)/2),0] = lam/h**2
print(rho)
A = Building_mat(n,n)
V = np.matmul(np.linalg.inv(A),-h**2*rho)
# print(rho)
# print(V)

plt.figure(figsize=(8,5))
plt.plot(np.linspace(0,n,n),V.reshape(n,n)[int((n-1)/2),::],marker='o',markersize=12,linestyle = '-',linewidth = 3,label='numerical')
# plt.plot(np.linspace(0,n,n),V.reshape(n,n)[int((n-1)/2),::],lw=3,color='r')
plt.legend(loc='best')
plt.show()