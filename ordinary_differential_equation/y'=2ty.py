import numpy as np
import matplotlib.pyplot as plt

# y'=2ty=g(y,t),y(1)=1
def Euler(yi,gi,h):
    return yi+h*gi

def g_function(ti,yi):
    return 2*ti*yi

N=130

initial=1
h=0.01
y0=1
t=[]
t.append(initial)
g0=2*t[0]*y0

y=[]
y.append(y0)
g=[]

for i in range(0,N):
    g.append(g_function(t[i],y[i]))
    y.append(Euler(y[i],g[i],h))
    t.append(t[i]+h)

plt.plot(t,y,"b.",label='RK2')
plt.plot(t,np.exp(np.asarray(t)**2-1),'r',label='analytic')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.title("$y'=2ty$ with $y(1)=1$")
plt.show()