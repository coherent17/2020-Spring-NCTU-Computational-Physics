import numpy as np
import matplotlib.pyplot as plt

def wave(n,nprime,x,w):
    return (2/w)*np.sin(n*np.pi/w*x)*x*np.sin(nprime*np.pi/w*x)

def rectangle_rule(initial,final,N,n,nprime,w):
    initial=initial
    final=final
    N=N
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in range(len(x)):
        y.append(wave(n,nprime,x[i],w)*h)
    return np.sum(y)

area=[]
for i in range(3,10+1):
    area.append(rectangle_rule(0,10*10**-9,1001,2,i,10*10**-9)**2)
ind=np.arange(3,11,1)
print(ind)
print(area)
plt.plot(ind,area)
plt.show()

