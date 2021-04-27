import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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

def rho(N,h,lam):
    rho=np.zeros((N**2,1))
    rho[int((N**2-1)/2),0]=lam/(h**2)
    return rho


L=1
N=51
h=L/(N-1)
lam=1
x=np.linspace(0,L,N)
A=coefficient_matrix(N)
rho=rho(N,h,lam)
V=(-h**2*np.linalg.inv(A)@rho)

#reshape the potential draw the middle of the potential
fig=plt.figure(figsize=(18,6))
ax1=fig.add_subplot(121)
V_temp=V.reshape(N,N)
ax1.plot(x,V_temp[int((N-1)/2),:])

#contourf
ax2=fig.add_subplot(122)
x_con=np.linspace(0,L,N)
y_con=np.linspace(0,L,N)
xx,yy=np.meshgrid(x_con,y_con)
z=V_temp
plt.contourf(xx,yy,z,cmap='rainbow')
plt.colorbar()
plt.show()

#contourf3D
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.contourf3D(xx,yy,z,levels=1001)
plt.show()