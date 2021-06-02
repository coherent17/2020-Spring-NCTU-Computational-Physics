import numpy as np
import matplotlib.pyplot as plt

#parameter:
m=2.3*(10**(-26))           #(kg)
𝛾=1.1*(10**12)              #(rad/s)
omega_0=5*2*np.pi*(10**12)  #(rad/s)
N=3*(10**28)                #(m^-3)
e=1.6*(10**(-19))           #(C)
omega=0.7*omega_0           #(rad/s)
E_0=70*(10**9)              #(V/m)
delta_t_inv=0.03*omega

#grid point setting:
initial=-50
final=50
N_p=1000
t=np.linspace(initial,final,N_p)
h=(t[1]-t[0])*np.pi/omega_0

#define the pulse electric field of the laser beam
def Electric_field(ti):
    A_E=E_0*np.exp(-((ti)/(1/delta_t_inv))**2)
    return A_E*np.cos(omega*ti)

#initial condition:
x0=0
v0=0

def g1(y2):
    return (y2)

def g2(y1,y2,ti):
    F=-1*e*Electric_field(ti)
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



x,v=Lorentz()
print(x)
#deal with the unit of x(t) and v(t)
for i in range(len(x)):
    x[i]=x[i]*(10**12)/1500
    v[i]=v[i]/30000

plt.plot(t,Electric_field(t*np.pi/omega_0)/E_0,label='$E(t)/E_0$')
plt.plot(t,x,label='$x(t)/1500(pm)$')
plt.xlabel('$\omega_0t/\pi$',fontsize=16)
# plt.plot(t,v)
plt.title("Pulse of the laser beam,$\omega/\omega_0=%.2f$,$\Delta_t^{-1}/\omega=%.2f$" %(omega/omega_0,delta_t_inv/omega),fontsize=20)
plt.legend(fontsize=16)
plt.show()