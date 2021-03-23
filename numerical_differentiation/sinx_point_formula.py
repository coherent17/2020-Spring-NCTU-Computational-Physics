import numpy as np
import matplotlib.pyplot as plt

N=51
x=np.linspace(-np.pi,np.pi,N)
h=2*np.pi/(N-1)

y1=np.sin(x)
dy1=np.cos(x)

#acclaim the data to store the var

dy2=np.zeros((N),dtype=float)
dy2f=np.zeros((N),dtype=float)

for i in range(1,N-1):
    dy2[i]=(y1[i+1]-y1[i-1])/2/h
    dy2f[i]=(y1[i+1]-y1[i])/h

#calculate the error
e2=np.abs(dy1-dy2)
e2f=np.abs(dy1-dy2f)

#visualize the approximation part
plt.plot(x,dy1,'r-',lw=3,label="analytic")
plt.plot(x,dy2,'b.',Markersize=5,label="central (three point)")
plt.plot(x,dy2f,'go',Markersize=5,label="two point")
# plt.xlim(-1.8,1.8)
plt.legend()
plt.show()

#visualize the error
plt.plot(x,e2,'r.',Markersize=5,label="three point error")
plt.plot(x,e2f,'b.',Markersize=5,label="two point error")
plt.xlim(-3.13,3.13)
plt.ylim(-0.1,0.2)
plt.legend()
plt.show()