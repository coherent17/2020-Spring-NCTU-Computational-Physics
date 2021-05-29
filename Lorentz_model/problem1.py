import numpy as np
import matplotlib.pyplot as plt

#fit the analytical formalism of refractive index in Lorentz model
#find 𝜒_𝑏𝑔 and 𝛾

#parameter of NacCl:
m=2.3*(10**(-26))     #kg
w_0=5*(10**12)      #Hz
N=3*(10**28)        #1/m^3
gamma=(10**50)  #1/s
X=50
e=1.6*(10**(-19))     #C
e_0=8.854*(10**(-12)) #F/m
N=1000
w=np.linspace(0,20,N)
print(w)

def refractive_index_ana(wi):
    return np.sqrt(1+((N*(e**2))/(e_0*m))*((w_0**2)-(wi**2))/(((w_0**2)-(wi**2)**2)+(gamma*wi)**2))

refractive_index=[]
for i in w:
    refractive_index.append(refractive_index_ana(i*(10**12)))

plt.plot(w,refractive_index)
print(refractive_index)
plt.show()

