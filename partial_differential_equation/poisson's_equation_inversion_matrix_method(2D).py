import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#parameter
L=1
N=51
h=L/(N-1)
lam=1 #linear density of the charge
x=np.linspace(0,L,N) #grid point

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
    rho[int((N**2-1)/2),0]=lam/(h**2) #delta function
    return rho

def main(): #calculate the potential by inversion matrix
    A=coefficient_matrix(N)
    rh=rho(N,h,lam)
    V=(-h**2*np.linalg.inv(A)@rh)
    return V

V=main()

#visualize
fig=plt.figure(figsize=(18,6))
ax1=fig.add_subplot(122)
V_temp=V.reshape(N,N)   #reshape the potential draw the middle of the potential
ax1.plot(x,V_temp[int((N-1)/2),:])
ax1.set_title('V distribution divide by $y=L/2 plane$')
ax1.set_xlabel('x')
ax1.set_ylabel('V')
ax1.grid(True)

#contourf
ax2=fig.add_subplot(121)
x_con=np.linspace(0,L,N)
y_con=np.linspace(0,L,N)
xx,yy=np.meshgrid(x_con,y_con)
z=V_temp
plt.contourf(xx,yy,z,cmap='rainbow')
plt.colorbar()
ax2.set_title('V plane contour')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()

#contourf3D
fig=plt.figure()
ax=plt.axes(projection='3d')
mappable=ax.contourf3D(xx,yy,z,levels=501,cmap='rainbow')
fig.colorbar(mappable, ax=ax,label='$V$')
ax.set_title('2D poisson equation with 3D contour')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()