import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

#parameter:
m=2.3*(10**(-26))           #(kg)
𝛾=1.15*(10**12)             #(rad/s)
omega_0=5*2*np.pi*(10**12)  #(rad/s)
N=3*(10**28)                #(m^-3)
e=1.6*(10**(-19))           #(C)      
omega=0.1*omega_0           #(rad/s)  <--------change here to simulate different omega
E_0=70*(10**9)              #(V/m)

#grid point setting:
initial=0
final=150
N_p=15000
t=np.linspace(initial,final,N_p)
h=(t[1]-t[0])*np.pi/omega_0

#initial condition:
x0=0
v0=0

def g1(y2):
    return (y2)

def g2(y1,y2,ti):
    F=-1*e*E_0*np.cos(omega*ti)
    return (F/m)-(𝛾*y2)-((omega_0**2)*y1)

#calculate the value of the next moment by RK2 method
def y_rk2(y1,y2,ti):#with (w1,w2,alpha,beta) = (0.5,0.5,1,1)
    k1=g1(y2)
    q1=g2(y1,y2,ti)
    k2=g1(y2+h*q1)
    q2=g2(y1+h*k1,y2+h*q1,ti+h)
    y1_prime=y1+h*(0.5*k1+0.5*k2)
    y2_prime=y2+h*(0.5*q1+0.5*q2)
    return y1_prime,y2_prime

def Lorentz():
    x=[]
    v=[]
    x.append(x0)
    v.append(v0)
    for j in range(len(t)-1):
        a,b=y_rk2(x[j],v[j],t[j]*np.pi/omega_0)
        x.append(a)
        v.append(b)
    return x,v

def Electric_field(t):
    t=t*np.pi/omega_0
    return E_0*np.cos(omega*t)/E_0

x,v=Lorentz()
v_diff=[]

#deal with the unit of x(t) and v(t)
for i in range(len(x)):
    x[i]=x[i]*(10**9)
    v[i]=v[i]/30000

#use two points method to get the value of v by dx/dt
for i in range(len(x)-1):
    v_diff.append((x[i+1]-x[i])/h)

plt.plot(t,x,color="red",label='$x(t)/nm$')
plt.plot(t,v,color="green",label='$v(t)/30000(m/s)$')
plt.plot(t,Electric_field(t),color="blue",label='$E(t)/E_0$')
plt.xlabel("$\omega_0t/\pi$",fontsize=16)
plt.title('Lorentz model solved with RK2, $\omega/\omega_0=%.2f$' %(omega/omega_0),fontsize=20)
plt.legend(loc='lower right',fontsize=16)
plt.ylim(-1,1)
plt.xlim(0,150)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()


#visualize the Magnification
x1=[0.1,0.5,0.7,0.75,0.9,0.95,0.97]
y1=[0.5,0.6,0.75,1.2,2.2,4.2,7.1]
x2=[1.03,1.05,1.1,1.25,2]
y2=[7,4.2,2.2,0.9,0.375]
plt.plot(x1,y1,label='(a),(b)')
plt.plot(x2,y2,label='(c),(d)')
plt.xlabel('$\omega/\omega_0$')
plt.ylabel('Amplitude of the x(t) at steady-state 1/(nm)')
plt.title("the Magnification relationship")
plt.legend()
plt.show()