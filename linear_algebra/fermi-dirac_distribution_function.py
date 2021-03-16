import numpy as np
import matplotlib.pyplot as plt
import math

k_B=8.6173*10**(-5)
x=np.linspace(-0.1,0.1,2100)
y_1=1/(np.exp(x/(k_B*4))+1)
y_2=1/(np.exp(x/(k_B*77))+1)
y_3=1/(np.exp(x/(k_B*300))+1)

plt.plot(x,y_1,'r',label="T=4K")
plt.plot(x,y_2,'b',label="T=77K")
plt.plot(x,y_3,'k',label="T=300K")
plt.legend()
plt.xlabel("$ε$")
plt.show()