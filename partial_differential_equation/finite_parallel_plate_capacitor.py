import numpy as np
import matplotlib.pyplot as plt

N=11
x=np.linspace(0,10,N)
y=np.linspace(0,10,N)
xx,yy=np.meshgrid(x,y)


#BC
V=np.zeros((11,11),dtype=float)

iteration=0
while(iteration<10):
    V_old=V
    for i in range(1,N-1):
        for j in range(1,N-1):
            #setting the parallel plate capacitor as the constant
            if j==3 and i>=3 and i<=7:
                V[j,i]=-1
            elif j==7 and i>=3 and i<=7:
                V[j,i]=1
            #relaxation method to solve the pde
            else:
                V[j,i]=0.25*(V[j,i-1]+V[j-1,i]+V[j+1,i]+V[j,i+1])
    iteration+=1
    V_new=V
    print(iteration)
    # #check the error before and after the iteration
    # if iteration%1==0:
    #     error=np.zeros((N,N),dtype=float)
    #     for i in range(0,N):
    #         for j in range(0,N):
    #             error[j,i]=abs(V_new[j,i]-V_old[j,i])
    #     print(error)
    #     if error.all()<10**-50:
    #         break
    

        
            
fig=plt.figure(figsize=(18,6))
ax=fig.add_subplot(121)
z=V
plt.contourf(xx,yy,z,cmap='rainbow',levels=51)
plt.colorbar()
ax.set_title('V plane contour')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax1=fig.add_subplot(122)
ax1.plot(x,V[:,2])
plt.show()   