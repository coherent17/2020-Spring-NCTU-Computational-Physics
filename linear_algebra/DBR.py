import numpy as np
import matplotlib.pyplot as plt
import cmath 

list=np.linspace(350,850,1000)
def DBR(layer):
    #to store the data of reflectance in different wavelength
    R=[]

    D_1=np.array([[1+0j,1+0j]
                 ,[2.35+0j,-2.35+0j]])

    D_2=np.array([[1+0j,1+0j]
                 ,[1.38+0j,-1.38+0j]])

    for i in list:
        P_1=np.array([[cmath.exp(-1j*(2.35*(2*cmath.pi*(550/(4*2.35))/i)+0j)),0+0j]
                    ,[0+0j,cmath.exp(1j*(2.35*(2*cmath.pi*(550/(4*2.35))/i)+0j))]])

        P_2=np.array([[cmath.exp(-1j*(1.38*(2*cmath.pi*(550/(4*1.38))/i)+0j)),0]
                    ,[0,cmath.exp(1j*(1.38*(2*cmath.pi*(550/(4*1.38))/i)+0j))]])
        #M=(D1^-1)D2P2(D2^-1)D1P1
        M=np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(np.linalg.pinv(D_1),D_2),P_2),np.linalg.pinv(D_2)),D_1),P_1)

        for j in range(layer):
            M=np.matmul(M,M)
        
        r=M[1,0]/M[0,0]
        R.append(r.real**2+r.imag**2)

    return R

R2=DBR(1)
R4=DBR(2)
R6=DBR(3)

plt.plot(list,R2,label="2 layers")
plt.plot(list,R4,label="4 layers")
plt.plot(list,R6,label="6 layers")
plt.title("VCSEL reflectance $R$ versus the wavelength $λ$")
plt.xlabel("wavelength $λ$  (nm)")
plt.ylabel("reflectance $R$")
plt.legend()
plt.show()