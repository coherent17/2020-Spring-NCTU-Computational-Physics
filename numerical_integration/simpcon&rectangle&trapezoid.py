import numpy as np
import matplotlib.pyplot as plt

#rectangle rule
#int 3x^2 from 0..10
#the analytic answer=1000
def function(x):
    return 1/(1+x**2)

def rectangle_rule(initial,final,N):
    initial=initial
    final=final
    N=N+1
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in x:
        y.append(function(i)*h)
    return np.sum(y)

#trapezoid rule (decrease the error from the rectangle rule)
def trapezoid_rule(initial,final,N):
    initial=initial
    final=final
    N=N+1
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in range(len(x)-1):
        y.append((function(x[i])+function(x[i+1]))*h/2)
    return np.sum(y)

def simpson_rule(initial,final,N):
    initial=initial
    final=final
    N=N+1
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            y.append((h/3)*function(x[i]))
        elif i%2==1:
            y.append((h/3)*4*function(x[i]))
        else:
            y.append((h/3)*2*function(x[i]))
    return (np.sum(y))

area=simpson_rule(0,1,4)
print(area)
area=rectangle_rule(0,1,4)
print(area)
area=trapezoid_rule(0,1,4)
print(area)