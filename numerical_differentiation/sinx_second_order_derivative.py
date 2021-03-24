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

ddy_3=[]
for i in range(1,N-1):
    ddy_3.append((y_ana[i+1]-2*y_ana[i]+y_ana[i-1])/h/h)

x3=np.delete(x,[0,N-1])

plt.plot(x,ddy_ana)
plt.plot(x3,ddy_3,'r.',label="three points")
plt.show()

error3=(abs(ddy_3-ddy_ana[1:N-1]))
plt.plot(x3,error3,label="three points")
plt.title("error by using different number of points")
plt.legend()
plt.show()