import numpy as np
import matplotlib.pyplot as plt

#rectangle rule
#int 3x^2 from 0..10
#the analytic answer=1000
def function(x):
    return 3*x**2

def error_percentage(exp,exat):
    return abs(exp-exat)/exp

def rectangle_rule(initial,final,N):
    initial=initial
    final=final
    N=N
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in x:
        y.append(function(i)*h)
    return np.sum(y)

#test the step vs the error and the percentage
test_step=np.arange(1,1100,100)
area=[]
error=[]
percentage=[]
for i in test_step:
    area.append(rectangle_rule(0,10,i))
    error.append(rectangle_rule(0,10,i)-1000)
    percentage.append((rectangle_rule(0,10,i)-1000)/(rectangle_rule(0,10,i)))

#visualize
fig=plt.figure(figsize=(18,6))
ax1=fig.add_subplot(121)
ax1.plot(test_step,error)
ax1.set_title("the step versus the error")
ax1.set_ylabel("error from the exact value")
ax1.set_xlabel("the steps")
ax1.grid(True)

ax2=fig.add_subplot(122)
ax2.plot(test_step,percentage)
ax2.set_title("the step versus the error percentage")
ax2.set_ylabel("error percentage")
ax2.set_xlabel("the steps")
ax2.grid(True)
plt.show()


#trapezoid rule (decrease the error from the rectangle rule)
def trapezoid_rule(initial,final,N):
    initial=initial
    final=final
    N=N
    h=(final-initial)/(N-1)
    x=np.linspace(initial,final,N)
    y=[]
    for i in range(len(x)-1):
        y.append((function(x[i])+function(x[i+1]))*h/2)
    return np.sum(y)

#test the step vs the error and the percentage
test_step=np.arange(100,1100,100)
area=[]
error=[]
percentage=[]
for i in test_step:
    area.append(trapezoid_rule(0,10,i))
    error.append(trapezoid_rule(0,10,i)-1000)
    percentage.append((trapezoid_rule(0,10,i)-1000)/(trapezoid_rule(0,10,i)))

#visualize
fig=plt.figure(figsize=(18,6))
ax1=fig.add_subplot(121)
ax1.plot(test_step,error)
ax1.set_title("the step versus the error")
ax1.set_ylabel("error from the exact value")
ax1.set_xlabel("the steps")
ax1.grid(True)

ax2=fig.add_subplot(122)
ax2.plot(test_step,percentage)
ax2.set_title("the step versus the error percentage")
ax2.set_ylabel("error percentage")
ax2.set_xlabel("the steps")
ax2.grid(True)
plt.show()