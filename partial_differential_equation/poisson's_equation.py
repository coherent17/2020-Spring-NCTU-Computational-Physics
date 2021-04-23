import numpy as np
import matplotlib.pyplot as plt

N=11
L=1
h=L/(N-1)
x=np.arange(0,N)
x=h*x
print(x)

V=np.zeros(N)

#poisson matrix
A=np.array(
[[1,0,0,0,0,0,0,0,0,0,0]
,[1,-2,1,0,0,0,0,0,0,0,0]
,[0,1,-2,1,0,0,0,0,0,0,0]
,[0,0,1,-2,1,0,0,0,0,0,0]
,[0,0,0,1,-2,1,0,0,0,0,0]
,[0,0,0,0,1,-2,1,0,0,0,0]
,[0,0,0,0,0,1,-2,1,0,0,0]
,[0,0,0,0,0,0,1,-2,1,0,0]
,[0,0,0,0,0,0,0,1,-2,1,0]
,[0,0,0,0,0,0,0,0,1,-2,1]
,[0,0,0,0,0,0,0,0,0,0,1]]
)

rho=np.zeros((N))
rho[int(N/2)]=1

B=np.linalg.inv(A)
V=-h*np.matmul(B,rho)
print(V)

plt.plot(x,V)
plt.xlabel('x(L)')
plt.ylabel('V ($\sigma/\epsilon_0 \epsilon_b$)')
plt.show()