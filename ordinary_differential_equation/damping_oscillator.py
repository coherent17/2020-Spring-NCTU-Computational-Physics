import numpy as np
import matplotlib.pyplot as plt

#ma+bv+kx=0 (no out force)
#define: (b/m)=r , (k/m)=w^2
#x''+rx'+(w^2)x=0
#dx/dt=v, dv/dt=-rv-(w^2)x
#define: tau=wt
#dx/dtau=v/w, dv/dtau=-(r/w)v-wx
#define: u=v/w
#dx/dtau=u
#du/dtau=-(r/w)u-x
#let y1=x, y2=u
#dy1/dtau=y2=g1, dy2/dtau=-(r/w)y2-y1=g2

#parameter:
gamma=[0.1,1,2,3] #damping coefficient
omega_0=1.0 # natural frequency
N=2000
h=0.01
t=np.arange(N)*h

#initial condition: x(0)=X0, v(0)=0
x0=1
v0=0


def g1(y1,y2):
    return (y2)

def g2(y1,y2,gamma_i):
    return (-y1-(gamma_i/omega_0)*y2)

#calculate the value of the next moment by RK2 method
def y_rk2(y1,y2,gamma_i):#with (w1,w2,alpha,beta) = (0.5,0.5,1,1)
    k1=g1(y1,y2)
    q1=g2(y1,y2,gamma_i)
    k2=g1(y1+h*k1,y2+h*q1)
    q2=g2(y1+h*k1,y2+h*q1,gamma_i)
    y1_prime=y1+h*(0.5*k1+0.5*k2)
    y2_prime=y2+h*(0.5*q1+0.5*q2)
    return y1_prime,y2_prime

def SHO(gamma_i):
    x=[]
    v=[]
    x.append(x0)
    v.append(v0)
    for i in range(0,N-1):
        a,b=y_rk2(x[i],v[i],gamma_i)
        x.append(a)
        v.append(b)
    return x,v

def visualize(x,v,gamma_i):
    plt.plot(t/np.pi, x, label="x(t)")
    plt.plot(t/np.pi, v, label="v(t)")
    plt.axhline(y=1, linestyle="--")
    plt.axhline(y=-1, linestyle="--")
    plt.title("RK2, SHO with $\gamma/\omega0=$%1.1f, x(0)=%1.1f,v(0)=%1.1f"%(gamma_i/omega_0, x0, v0))
    plt.xlabel("$t/\pi$")
    plt.ylabel("$y_n(t)$")
    plt.legend()
    plt.show()

#main function:
for j in gamma:
    x,v=SHO(j)
    visualize(x,v,j)