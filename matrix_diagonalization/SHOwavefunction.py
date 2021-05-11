import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermval

x=np.linspace(-3,3,1001)
def Hermite(n):
    matrix=np.zeros((n+1,))
    matrix[n]=1
    return hermval(x,matrix)

def factorial(n):
    value=1
    for i in range(1,n+1):
        value*=i
    return value

def Wave(n):
    return (1/np.pi)**0.25*1/np.sqrt((2**n)*factorial(n))*Hermite(n)*np.exp(-1*(x**2)/2)

W0=Wave(0)
W1=Wave(1)
W2=Wave(2)

plt.plot(x,W0)
plt.plot(x,W1)
plt.plot(x,W2)

plt.show()