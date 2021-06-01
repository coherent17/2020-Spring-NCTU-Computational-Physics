import numpy as np
import matplotlib.pyplot as plt

#parameter:
m=2.3*(10**(-26))           #(kg)
𝛾=1.1*(10**12)              #(rad/s)
omega_0=5*2*np.pi*(10**12)  #(rad/s)
N=3*(10**28)                #(m^-3)
e=1.6*(10**(-19))           #(C)
omega=0.1*omega_0           #(rad/s)
E_0=70*(10**9)              #(V/m)

#grid point setting:
initial=-25
final=50
N_p=15000
t=np.linspace(initial,final,N_p)
h=(t[1]-t[0])*np.pi/omega_0

def Electric_field(ti):
    A_E=3*np.exp(-1*((ti)/8)**2)
    return A_E*np.cos(8*ti)

plt.plot(t,Electric_field(t-25))
plt.show()

