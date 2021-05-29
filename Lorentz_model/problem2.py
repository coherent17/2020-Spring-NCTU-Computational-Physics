import numpy as np
import matplotlib.pyplot as plt

#parameter:
m=2.3*(10**-26) #(kg)
gamma=5000
omega_0=5*(10**12)  #(Hz)
N=3000 
h=0.01
e=1.6*(10**-19) #(C)
omega=5
E_0=5
t=np.arange(N)*h

#initial condition:
x0=5
v0=0

def g1(y1,y2):
    return y2

def g2(y1,y2,ti):
    F=-1*e*E_0*np.cos(omega*ti)
    return (F/m)-gamma*y2-(omega_0**2)*y1

def y_rk2(y1,y2,ti):
    k1=g1(y1,y2)
    q1=g2(y1,y2,ti)
    k2=g1(y1+h*k1,y2+h*q1)
    q2=g2(y1+h*k1,y2+h*q1,ti)
    y1_prime=y1+h*(0.5*k1+0.5*k2)
    y2_prime=y2+h*(0.5*q1+0.5*q2)
    return y1_prime,y2_prime

def Lorentz():
    x=[]
    v=[]
    x.append(x0)
    v.append(v0)
    for i in range(0,N-1):
        a,b=y_rk2(x[i],v[i],t[i])
        x.append(a)
        v.append(b)
    return x,v

def visualize(x,v,):
    plt.plot(t/np.pi, x)
    plt.plot(t/np.pi, v)
    plt.xlabel("$t/\pi$")
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend()
    plt.show()

x,v=Lorentz()
print(x)