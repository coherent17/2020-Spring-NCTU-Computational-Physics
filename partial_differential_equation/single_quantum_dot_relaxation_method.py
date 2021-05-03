import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt

#parameter
N=41
x=np.linspace(0,40,N)
z=np.linspace(0,40,N)
xx,zz=np.meshgrid(x,z)
omg=0.9 #sor coefficient

def BC_GC():
    #Boundary condition
    V=np.zeros((N,N),dtype=float)
    #Gate condition
    V[20,5:16]=1
    V[20,25:36]=1
    return V

def FDM1(eps):
    iteration=0
    V_old=BC_GC()
    V_new=BC_GC()
    while(True):
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
        if (abs(V_new-V_old)<eps).all()==True:
            print(iteration)
            break
        V_old=V_new.copy()
    return V_new,iteration

def FDM2(n):
    iteration=0
    V_old=BC_GC()
    V_new=BC_GC()
    while(iteration<n):
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
        # V_new=omg*V_new+(1-omg)*V_old
        iteration+=1
        V_old=V_new.copy()
    return V_new

def contour_draw(V):
    #electrostatic potential and electric field
    fig=plt.figure(figsize=(18,6))
    ax=fig.add_subplot(121)
    y=V
    plt.contourf(xx,zz,y,cmap='rainbow',levels=51)
    v,u=np.gradient(y)
    ax.quiver(xx,zz,-u,-v)
    plt.colorbar()
    ax.set_title('V plane contour')
    ax.set_xlabel('x')
    ax.set_ylabel('z')

    #section
    z=16
    ax1=fig.add_subplot(122)
    ax1.plot(x,V[z,:])
    ax1.set_title('z=%d section' %(z))
    ax1.set_xlabel('x')
    ax1.set_ylabel('V')
    plt.show()

def contour_iter_draw(iteration_list,V_iter):
    fig=plt.figure(figsize=(18,6))
    ax=['ax1','ax2','ax3','ax4','ax5','ax6','ax7','ax8']

    for i in range(8):
        ax[i]=fig.add_subplot(2,4,i+1)
        plt.contourf(xx,zz,V_iter[i],cmap='rainbow',levels=51)
        plt.colorbar()
        ax[i].set_title('iteration:'+str(iteration_list[i]),fontsize=10)
    plt.show()

#comparison between the iteration time and with sor coefficient = 1
iteration_list=[0,5,15,30,50,100,250,500]
V_iter=[]
for i in iteration_list:
    V_iter.append(FDM2(i))
contour_iter_draw(iteration_list, V_iter)

#setting the eps to stop the infinite loop with sor method:
V_FDM,iteration=FDM1(0.001)
contour_draw(V_FDM)

#3D contour
fig=plt.figure()
ax=plt.axes(projection='3d')
mappable=ax.contourf3D(xx,zz,V_FDM,levels=51,cmap='rainbow')
fig.colorbar(mappable, ax=ax,label='$V$')
ax.set_title('single quantum dot with 3D contour')
ax.set_xlabel('x')
ax.set_ylabel('z')
plt.show()