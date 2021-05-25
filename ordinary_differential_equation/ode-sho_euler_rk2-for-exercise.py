# solve a SHO: Euler rule and RK2

import numpy as np
import matplotlib.pyplot as plt
    
####################### g(y1,y2,t) for SHO's ODEs
gamma=0.0 #  damping (global variable)
omega0=1.0 # nat. ang. freq. (global)

def g1(y1,y2,t):
    g=...
    return (g)

def g2(y1,y2,t):
    g=...
    return (g) 


def y_euler(y1i,y2i,ti,h): #y_i+1 given by Euler rule
    y1_ip1=...
    y2_ip1=...
    return (y1_ip1,y2_ip1) 


########################


######################## solve SHO
def sho(x0,v0,t0,h,Nh):
    x=np.zeros(Nh)
    v=np.zeros(Nh)
    t=np.arange(Nh)
    t=h*t+t0
    x[0]=x0
    v[0]=v0
    for i in range(0,Nh-1):
        #x[i+1], v[i+1]=y_euler(x[i],v[i],t[i],h)
        x[i+1], v[i+1]=y_rk2(x[i],v[i],t[i],h,0.5,0.5,1.,1.) # RK2
    return (x,v,t)
########################


######################## main code

tt0=0.0; xx0=0.0; vv0=1.0 # initial condition 
h=0.1;N=200 

xx=np.zeros(N)
vv=np.zeros(N)
tt=np.zeros(N)

xx,vv,tt=sho(xx0,vv0,tt0,h,N)
    
   
####################### plot
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(tt/np.pi, xx, label="x(t)")
ax.plot(tt/np.pi, vv, label="v(t)")

ax.axhline(y=1, linestyle="--")
ax.axhline(y=-1, linestyle="--")
ax.set_title(\
             "RK2, SHO with $\gamma/\omega0=$%1.1f/%1.1f, x(0)=%1.1f,v(0)=%1.1f"\
             %(gamma,omega0, xx0, vv0),fontsize=20)
    # "\": change line
plt.xlabel("$t/\pi$",fontsize=25)
plt.ylabel("$y_n(t)$",fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#plt.ylim(0.0,1.1)
ax.legend(fontsize=25)
plt.show()
