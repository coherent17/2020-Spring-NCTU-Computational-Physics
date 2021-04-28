import numpy as np
np.set_printoptions(threshold=10000000000)
import matplotlib.pyplot as plt

#parameter
N=41
x=np.linspace(0,40,N)
z=np.linspace(0,40,N)
xx,zz=np.meshgrid(x,z)
omg=1 #sor coefficient

#Boundary condition
V=np.zeros((N,N),dtype=float)
#Gate condition
V[20,5:16]=1
V[20,25:36]=1

iteration=0
V_old=V
while(True):
    V_new=V_old
    for i in range(1,N-1):
        for j in range(1,N-1):
            #setting the gate condition as the constant
            if (i>=5 and i<=15) and j==20:
                continue
            elif (i>=25 and i<=35) and j==20:
                continue
            #relaxation method
            else:
                V_new[j,i]=0.25*(V_old[j,i-1]+V_old[j-1,i]+V_old[j+1,i]+V_old[j,i+1])
    V_new=omg*V_new+(1-omg)*V_old
    iteration+=1
    #set the eps to break the while loop
    if iteration%1000==0:
        if abs(V_new-V_old).all()<10**-10:
            print(iteration)
            break

fig=plt.figure(figsize=(18,6))
ax=fig.add_subplot(121)
y=V
plt.contourf(xx,zz,y,cmap='rainbow',levels=51)
plt.colorbar()
ax.set_title('V plane contour')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax1=fig.add_subplot(122)
ax1.plot(x,V[16,:])
plt.show()   