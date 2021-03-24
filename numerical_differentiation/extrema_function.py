import numpy as np
import matplotlib.pyplot as plt

N=10001
initial=-np.pi
final=np.pi
x=np.linspace(initial,final,N)
h=(final-initial)/(N-1)

y=np.sin(x)
dy=np.cos(x)
ddy=-np.sin(x)

#first differential
dy_2=[]
for i in range(0,N-1):
    dy_2.append((y[i+1]-y[i])/h)

dx2=np.delete(x,[N-1])

#second differential
ddy_3=[]
for i in range(1,N-1):
    ddy_3.append((y[i+1]-2*y[i]+y[i-1])/h/h)

ddx3=np.delete(x,[0,N-1])


# get the extrema
y_max=[]
y_min=[]
for i in range(0,len(dy_2)-1):
    if dy_2[i]*dy_2[i+1]<=0:
        if ddy_3[i]>0:
            y_min.append(dx2[i])
        else:
            y_max.append(dx2[i])

#visualize
fig, axs = plt.subplots(3,sharex=True) 

axs[0].plot(x,y)
axs[0].plot(y_min,np.sin(y_min),"r.")
axs[0].plot(y_max,np.sin(y_max),"k.")
axs[0].set_title("$y=sinx$")

axs[1].plot(x,dy)
axs[1].plot(dx2,dy_2,'r.')
axs[1].set_title("$y'=cosx$")

axs[2].plot(x,ddy)
axs[2].plot(ddx3,ddy_3,'r.')
axs[2].set_title("$y''=sinx$")
plt.show()
