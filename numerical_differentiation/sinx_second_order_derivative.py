import numpy as np
import matplotlib.pyplot as plt

N=51
initial=-np.pi
final=np.pi
x=np.linspace(initial,final,N)
h=(final-initial)/(N-1)


#analytic:
y_ana=np.sin(x)
dy_ana=np.cos(x)
ddy_ana=-np.sin(x)

ddy_2=[]
for i in range(1,N-1):
    ddy_2.append((y_ana[i+1]-2*y_ana[i]+y_ana[i-1])/h/h)

x2=np.delete(x,[0,N-1])

plt.plot(x,ddy_ana)
plt.plot(x2,ddy_2,'r.',label="two points")
plt.show()