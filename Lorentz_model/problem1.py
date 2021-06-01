import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

#fit the analytical formalism of refractive index in Lorentz model
#find 𝜒_𝑏𝑔 and 𝛾

#parameter of NaCl:
# temp=np.linspace(1,2,50)
𝜒_𝑏𝑔=1.1
m=2.3*(10**(-26))            #(kg)
omega_0=5*2*np.pi*(10**12)   #(rad/s)
N=3*(10**28)                 #(m^-3)
𝛾=1.1*(10**12)                 #(rad/s)
e=1.6*(10**(-19))            #(C)
ε_0=8.854*(10**-12)          #(Farad/m)

#define k=(Ne^2)/(ε_0m)
k=N*(e**2)/(ε_0*m)

#grid points
initial=0
final=20
N_p=1000
omega=np.linspace(initial,final,N_p)

def refractive_index(omega):
    ε_1=1+𝜒_𝑏𝑔+k*((omega_0**2)-(omega**2))/((((omega_0**2)-(omega**2))**2)+((𝛾*omega)**2))
    if ε_1<0:
        ε_1=0
    return np.sqrt(ε_1)

n=[]
for i in range(len(omega)):
    n.append(refractive_index(omega[i]*2*np.pi*(10**12)))
print(n)
plt.plot(omega,n)
plt.xlabel('Frequency ($10^{12}Hz$)')
plt.ylabel('Refractive index')
plt.title('$NaCl$ frequency - refractive index')
plt.ylim(0,8)
plt.grid(True)
plt.show()