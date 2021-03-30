import numpy as np
import matplotlib.pyplot as plt

N=100001
initial=1
final=2000
x=np.linspace(initial,final,N)
h=(final-initial)/(N-1)

def Wien(T):
    y=[]
    for i in x:
        k=1.380649*(10**-23)
        hc=1.98644586*(10**-25)
        #*(10**-3):J->kJ
        #*(10**9):m->nm
        y.append(8*np.pi*hc/((i*(10**-9))**5)/(np.exp(hc/(i*(10**-9))/k/T)-1)*(10**-3))
    return y


def get_max_lamda(y_T):
    #first differential
    dy_2=[]
    for i in range(0,N-1):
        dy_2.append((y_T[i+1]-y_T[i])/h)

    dx2=np.delete(x,[N-1])

    #second differential
    ddy_3=[]
    for i in range(1,N-1):
        ddy_3.append((y_T[i+1]-2*y_T[i]+y_T[i-1])/h/h)

    ddx3=np.delete(x,[0,N-1])


    # get the extrema
    y_max=[]
    for i in range(0,len(dy_2)-1):
        if dy_2[i]*dy_2[i+1]<=0:
            if ddy_3[i]<0:
                y_max.append(dx2[i])

    return y_max

#obtain the intensity in different temperature
y_3500=Wien(3500)
y_4000=Wien(4000)
y_4500=Wien(4500)
y_5000=Wien(5000)
y_5500=Wien(5500)

#get the max lambda at different temperature unit:(nm)
l_3500=get_max_lamda(y_3500)
l_4000=get_max_lamda(y_4000)
l_4500=get_max_lamda(y_4500)
l_5000=get_max_lamda(y_5000)
l_5500=get_max_lamda(y_5500)

#get the constant of the wein's law unit:(mm*K)
print("At 3500K,\tλ_max=%.5f(nm)"%(l_3500[0]),"\t","λ_max*T=%.6f(mm*K)"%(l_3500[0]*3500*(10**-6)))
print("At 4000K,\tλ_max=%.5f(nm)"%(l_4000[0]),"\t","λ_max*T=%.6f(mm*K)"%(l_4000[0]*4000*(10**-6)))
print("At 4500K,\tλ_max=%.5f(nm)"%(l_4500[0]),"\t","λ_max*T=%.6f(mm*K)"%(l_4500[0]*4500*(10**-6)))
print("At 5000K,\tλ_max=%.5f(nm)"%(l_5000[0]),"\t","λ_max*T=%.6f(mm*K)"%(l_5000[0]*5000*(10**-6)))
print("At 5500K,\tλ_max=%.5f(nm)"%(l_5500[0]),"\t","λ_max*T=%.6f(mm*K)"%(l_5500[0]*5500*(10**-6)))
λmax_avg=np.mean([l_3500[0]*3500*(10**-6),l_4000[0]*4000*(10**-6),l_4500[0]*4500*(10**-6),l_5000[0]*5000*(10**-6),l_5500[0]*5500*(10**-6)])
print("the average of the Wien's distribution law is=%.5f(mm*K)"%(λmax_avg))

plt.plot(x,y_3500,label="$3500K$")
plt.plot(x,y_4000,label="$4000K$")
plt.plot(x,y_4500,label="$4500K$")
plt.plot(x,y_5000,label="$5000K$")
plt.plot(x,y_5500,label="$5500K$")
plt.title("Wien's law")
plt.xlabel("wavelength(λ) (nm)")
plt.ylabel("Spectral energy density ($kJ/m^4$)")
plt.text(1250,400,"$λ_{max}*T=%.3lf(mm*K)$"%(λmax_avg))
plt.legend()
plt.show()