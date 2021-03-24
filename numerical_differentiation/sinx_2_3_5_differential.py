import numpy as np
import matplotlib.pyplot as plt

N=101
initial=-np.pi
final=np.pi
x=np.linspace(initial,final,N)
h=(final-initial)/(N-1)

#analytic:
y_ana=np.sin(x)
dy_ana=np.cos(x)

#acclaim the list to store the data
dy_2=[]
dy_3=[]
dy_5=[]

for i in range(0,N-1):
    dy_2.append((y_ana[i+1]-y_ana[i])/h)

x2=np.delete(x,[N-1])

for i in range(1,N-1):
    dy_3.append((y_ana[i+1]-y_ana[i-1])/h/2)

x3=np.delete(x,[0,N-1])

for i in range(2,N-2):
    dy_5.append((y_ana[i-2]-8*y_ana[i-1]+8*y_ana[i+1]-y_ana[i+2])/12/h)

x5=np.delete(x,[0,1,N-2,N-1])

plt.plot(x,dy_ana,label="analytic")
plt.plot(x2,dy_2,'r.',label="two points")
plt.plot(x3,dy_3,'k.',label="three points")
plt.plot(x5,dy_5,'g.',label="five points")
plt.legend()
plt.show()

#error calculation
error2=(abs(dy_2-dy_ana[0:N-1]))
error3=(abs(dy_3-dy_ana[1:N-1]))
error5=(abs(dy_5-dy_ana[2:N-2]))

plt.plot(x2,error2,label="two points")
plt.plot(x3,error3,label="three points")
plt.plot(x5,error5,label="five points")
plt.title("error by using different number of points")
plt.legend()
plt.show()