import numpy as np
import matplotlib.pyplot as plt

#parameter:
initial=0
final=50
N=1001
t=np.linspace(initial,final,N)
h=(final-initial)/(N-1)
g=9.8 #(m/s^2)
D=0.1 #(kg*m)
m=70  #(kg)

#formula:
#mg-Dv^2=ma ->a=g-(D/m)*v^2 -> dv/dt= g-(D/m)*v^2 =U(v,t)

def U_function(vi):
    return g-(D/m)*(vi**2)

def Euler(vi,Ui):
    return vi+h*Ui

def RK2(vi): #with (w1,w2,alpha,beta) = (0.5,0.5,1,1)
    k1=U_function(vi)
    k2=U_function(vi+1*h*k1)
    return vi+h*(0.5*k1+0.5*k2)

def initial_condition(): #V(0)=0
    v_euler=[]
    U_euler=[]

    v_euler.append(0)
    U_euler.append(U_function(v_euler[0]))

    v_RK2=[]
    U_RK2=[]

    v_RK2.append(0)
    U_RK2.append(U_function(v_RK2[0]))
    return  v_euler,U_euler,v_RK2,U_RK2

def Euler_method(v_euler,U_euler):
    for i in range(0,N-1):
        U_euler.append(U_function(v_euler[i]))
        v_euler.append(Euler(v_euler[i],U_euler[i]))
    return v_euler

def RK2_method(v_RK2,U_RK2):
    for i in range(0,N-1):
        U_RK2.append(U_function(v_RK2[i]))
        v_RK2.append(RK2(v_RK2[i]))
    return v_RK2

def terminal_speed():
    V_terminal=[]
    for i in range(0,N):
        V_terminal.append(np.sqrt(m*g/D))
    return V_terminal

def visualize(v_euler,v_RK2,V_terminal):
    fig=plt.figure(figsize=(18,6))
    ax1=fig.add_subplot(121)
    ax1.plot(t,v_euler,label='euler method')
    ax1.plot(t,v_RK2,label='RK2 method')
    ax1.plot(t,V_terminal,label='terminal speed (analytic)')
    ax1.set_xlabel('t(sec)')
    ax1.set_ylabel('V(m/s)')
    ax1.set_title('falling object subject to air drag')
    ax1.grid(True)
    ax1.legend(loc='lower right')

    ax2=fig.add_subplot(122)
    ax2.plot(t,v_euler/V_terminal[0],label='euler method')
    ax2.plot(t,v_RK2/V_terminal[0],label='RK2 method')
    ax2.set_xlabel('t(sec)')
    ax2.set_ylabel('$V/V_{terminal}$')
    ax2.set_title('falling object subject to air drag')
    ax2.grid(True)
    ax2.legend(loc='lower right')
    plt.show()

v_euler,U_euler,v_RK2,U_RK2=initial_condition()
v_euler=Euler_method(v_euler,U_euler)
v_RK2=RK2_method(v_RK2,U_RK2)
V_terminal=terminal_speed()
visualize(v_euler,v_RK2,V_terminal)