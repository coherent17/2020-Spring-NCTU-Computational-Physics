import numpy as np
import matplotlib.pyplot as plt

N=150
Ng=2*N+1
dx=0.1
H=np.zeros((Ng,Ng),dtype=float)
for n in range(0,Ng):
    for m in range(0,Ng):
        if m==n: #mid
            x=dx*(n-N) #the position
            H[n,m]=1/(dx**2)+0.5*(x**2)
        elif m==n-1 or m==n+1: #left and right
            H[n,m]=-0.5/(dx**2)

eigenvalue,eigenvector=np.linalg.eig(H)
idx=np.argsort(eigenvalue)
eigenvalue=eigenvalue[idx]
eigenvector=eigenvector[:,idx]

fig=plt.figure(figsize=(18,6))
ax1=fig.add_subplot(121)
x=np.linspace(0,10,11)
y=(x+0.5)
ax1.plot(x,eigenvalue[0:11],'r.',label='numerical')
ax1.plot(x,y,label='analytical')
ax1.set_xlabel('n')
ax1.set_ylabel('$E_n/ħw_0$')
ax1.set_title('eigen energies')
ax1.grid(True)
ax1.legend()

ax2=fig.add_subplot(122)
x=np.linspace(-5,5,301)
y1=eigenvector[:,0]
y2=eigenvector[:,1]
y3=eigenvector[:,2]
y4=eigenvector[:,3]
y5=eigenvector[:,4]
ax2.plot(x,(y1**2),label='$Ψ_{n=0}(x)$')
ax2.plot(x,(y2**2),label='$Ψ_{n=1}(x)$')
ax2.plot(x,(y3**2),label='$Ψ_{n=2}(x)$')
ax2.plot(x,(y4**2),label='$Ψ_{n=3}(x)$')
# ax2.plot(x,np.sqrt(y5**2),label='$Ψ_{n=4}(x)$')
ax2.plot(x,0.5*(x**2),label='potential')
ax2.set_xlabel('position (x)')
ax2.set_ylabel('wave function square')
ax2.set_title('The probability of the lowest eigen state')
ax2.set_ylim(0,0.06)
ax2.set_xlim(-2,2)
ax2.legend()
ax2.grid(True)
plt.show()



