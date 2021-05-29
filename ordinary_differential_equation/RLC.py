import numpy as np
import matplotlib.pyplot as plt

#parameter:
e=300 #charge voltage (volt)
R=0.8 #(ohm)
L=2.5 #(h)
C=0.3 #(F)
N=3000 
h=0.01
t=np.arange(N)*h
omega=10000

#initial condition:
q0=C*e
i0=0.0

def g1(y1,y2):
    return (-y2)

def g2(y1,y2,ti):
    return 1/(L*C)*y1-(R/L)*y2-e/L*np.cos(omega*ti)


#calculate the value of the next moment by RK2 method
def y_rk2(y1,y2,ti):#with (w1,w2,alpha,beta) = (0.5,0.5,1,1)
    k1=g1(y1,y2)
    q1=g2(y1,y2,ti)
    k2=g1(y1+h*k1,y2+h*q1)
    q2=g2(y1+h*k1,y2+h*q1,ti)
    y1_prime=y1+h*(0.5*k1+0.5*k2)
    y2_prime=y2+h*(0.5*q1+0.5*q2)
    return y1_prime,y2_prime

def SHO():
    q=[]
    i=[]
    V_c=[]
    q.append(q0)
    i.append(i0)
    V_c.append(q0/C)
    for j in range(0,N-1):
        a,b=y_rk2(q[j],i[j],t[j])
        q.append(a)
        i.append(b)
        V_c.append(np.abs(a/C))
    return q,i,V_c

def visualize(q,i,V_c):
    plt.plot(t/np.pi, q, label="$q(t) (C)$")
    plt.plot(t/np.pi, i, label="$i(t) (A)$")
    plt.plot(t/np.pi, V_c, label="$|V_c(t)| (V)$")
    plt.title("RLC circuit with RK2 method")
    plt.xlabel("$t/\pi$")
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend()
    plt.show()

q,i,V_c=SHO()
visualize(q,i,V_c)