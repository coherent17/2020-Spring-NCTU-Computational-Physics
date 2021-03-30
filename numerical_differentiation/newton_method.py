import numpy as np 
import matplotlib.pyplot as plt 

N=1001
initial=-6
final=6
h=(final-initial)/(N-1)
x=np.linspace(initial,final,1001)
y=(x**2)-3*x-10

#first order differential
dy_2=[]
for i in range(0,N-1):
    dy_2.append((y[i+1]-y[i])/h)
x2=np.delete(x,[N-1])

def f(x):
    return (x**2)-3*x-10

def newton(x_0,eps):
    iteration=0
    while 1:
        if abs(f(x_0))>eps:
            x_0=x_0-f(x_0)/dy_2[int((x_0-initial)/h)]
            print(x_0)
            iteration+=1
        else:
            break
    return x_0,iteration

root,iteration=newton(4,0.0000001)
print(root)
print(iteration)