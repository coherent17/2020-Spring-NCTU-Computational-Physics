import numpy as np
import matplotlib.pyplot as plt

def wave(n,nprime,x,w):
    return (2/w)*np.sin(nprime*np.pi/w*x)*x*np.sin(n*np.pi/w*x)

def simpson_rule(initial,final,N,n,nprime,w):
    initial=initial
    final=final
    N=N+1
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            y.append((h/3)*wave(n,nprime,x[i],w))
        elif i%2==1:
            y.append((h/3)*4*wave(n,nprime,x[i],w))
        else:
            y.append((h/3)*2*wave(n,nprime,x[i],w))
    return (np.sum(y))

def rectangle_rule(initial,final,N,n,nprime,w):
    initial=initial
    final=final
    N=N+1
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in x:
        y.append(wave(n,nprime,i,w)*h)
    return np.sum(y)

def trapezoid_rule(initial,final,N,n,nprime,w):
    initial=initial
    final=final
    N=N+1
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in range(len(x)-1):
        y.append((wave(n,nprime,x[i],w)+wave(n,nprime,x[i+1],w))*h/2)
    return np.sum(y)

#simpson_rule & rectangle rule & trapezoid rule
#store the area of the integral in different energy level
area_s=[]#simpson
area_r=[]#rectangle
area_t=[]#trapezoid
for i in range(2,10+1):
    area_s.append(simpson_rule(0,10,500,1,i,10)**2)
    area_r.append(rectangle_rule(0,10,500,1,i,10)**2)
    area_t.append(trapezoid_rule(0,10,500,1,i,10)**2)

#visualize
# (simpson part)
ind=np.arange(2,11,1)
fig=plt.figure(figsize=(18,20))
ax1=plt.subplot2grid((5,2),(0,0))
ax1.plot(ind,area_s)
ax1.set_title("selection rule by simpson rule",fontsize=10)
ax1.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax1.set_xlabel("$n^{\prime}$")
ax1.grid(True)

ax2=plt.subplot2grid((5,2),(0,1))
ax2.plot(ind[1:],area_s[1:])
ax2.set_title("selection rule by simpson rule (room in)",fontsize=10)
ax2.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax2.set_xlabel("$n^{\prime}$")
ax2.grid(True)

# (rectangle part)
ax3=plt.subplot2grid((5,2),(2,0))
ax3.plot(ind,area_r)
ax3.set_title("selection rule by rectangle rule",fontsize=10)
ax3.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax3.set_xlabel("$n^{\prime}$")
ax3.grid(True)

ax4=plt.subplot2grid((5,2),(2,1))
ax4.plot(ind[1:],area_r[1:])
ax4.set_title("selection rule by rectangle rule (room in)",fontsize=10)
ax4.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax4.set_xlabel("$n^{\prime}$")
ax4.grid(True)

# (trapezoid part)
ax5=plt.subplot2grid((5,2),(4,0))
ax5.plot(ind,area_t)
ax5.set_title("selection rule by trapezoid rule",fontsize=10)
ax5.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax5.set_xlabel("$n^{\prime}$")
ax5.grid(True)

ax6=plt.subplot2grid((5,2),(4,1))
ax6.plot(ind[1:],area_t[1:])
ax6.set_title("selection rule by trapezoid rule (room in)",fontsize=10)
ax6.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax6.set_xlabel("$n^{\prime}$")
ax6.grid(True)

plt.show()

#all in one graph:
fig=plt.figure(figsize=(18,6))
ax1=fig.add_subplot(121)
ax1.plot(ind,area_t,label="trapezoid rule")
ax1.plot(ind,area_r,label="rectangle rule")
ax1.plot(ind,area_s,label="simpson rule")
ax1.set_title("different method",fontsize=10)
ax1.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax1.set_xlabel("$n^{\prime}$")
ax1.grid(True)
ax1.legend()

ax2=fig.add_subplot(122)
ax2.plot(ind[1:],area_t[1:],label="trapezoid rule")
ax2.plot(ind[1:],area_r[1:],label="rectangle rule")
ax2.plot(ind[1:],area_s[1:],label="simpson rule")
ax2.set_title("different method (zoom in)",fontsize=10)
ax2.set_ylabel("$\\vert V_{n^{\prime}n}^2 \\vert$")
ax2.set_xlabel("$n^{\prime}$")
ax2.grid(True)
ax2.legend()

plt.show()