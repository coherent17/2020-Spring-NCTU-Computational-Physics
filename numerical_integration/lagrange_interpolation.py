import numpy as np
import matplotlib.pyplot as plt
import math

x=np.array([0,1/6,1/3])
y=np.array([1,np.sqrt(3)/2,0.5])


def lagrange_interpolation(a,x,y):
    return (a-x[1])*(a-x[2])/(x[0]-x[1])/(x[0]-x[2])*y[0]+\
    (a-x[0])*(a-x[2])/(x[1]-x[0])/(x[1]-x[2])*y[1]+\
    (a-x[0])*(a-x[1])/(x[2]-x[0])/(x[2]-x[1])*y[2]

def fcos(x):
    return np.cos(x*np.pi)

x_test=np.linspace(0,0.5,2001)
f=lagrange_interpolation(x_test,x,y)
plt.plot(x_test,f,label='2nd order Lagrange')
plt.plot(x_test,fcos(x_test),label='exact')
plt.plot(x,y,'bo',label='data')
plt.title('n-order Lagrange interpolation for\n $f(x_i)=cos(i*π/6),i=0,1,2,n=2$')
plt.xlabel('$x_i/π$')
plt.ylabel('$f(x)$')
plt.legend()
plt.show()