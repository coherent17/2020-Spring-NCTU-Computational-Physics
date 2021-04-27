import numpy as np
import matplotlib.pyplot as plt

#plus delta to avoid the singular points
def electric_potential(xx,yy):
    delta=0.0001
    return 1/np.sqrt(xx**2+yy**2+delta)

def dVx(xx,yy):
    delta=0.0001
    return 1*xx/np.sqrt(xx**2+yy**2+delta)

def dVy(xx,yy):
    delta=0.0001
    return 1*yy/np.sqrt(xx**2+yy**2+delta)

N=51
x=np.linspace(-1,1,N)
y=np.linspace(-1,1,N)
xx,yy=np.meshgrid(x,y)

fig=plt.figure()
ax = fig.add_subplot(1,1,1)
c=ax.contourf(xx,yy,electric_potential(xx, yy),levels=501,cmap='rainbow')
ax.quiver(xx,yy,dVx(xx,yy),dVy(xx,yy),width=0.001)
fig.colorbar(c, ax=ax)
ax.set_title('point charge electric field')
ax.set_xlabel('x')
ax.set_xlim(-0.5,0.5)
ax.set_ylim(-0.5,0.5)
plt.show()