import numpy as np
import matplotlib.pyplot as plt

N=51
x=np.linspace(0,5,N)
h=5/(N-1)
vy=1-np.exp(-x)

plt.plot(x,vy,label="$v_y/v_t$")
plt.title("Falling object in a fluid")
plt.legend()
plt.show()

dvy_ana=1-vy
dvy_2=[]
for i in range(0,N-1):
    dvy_2.append((vy[i+1]-vy[i])/h)
x2=np.delete(x,[N-1])


plt.plot(x,dvy_ana,label="$(1-v_y)/t_s$")
plt.plot(x2,dvy_2,'r.',label="two points")
plt.legend()
plt.show()