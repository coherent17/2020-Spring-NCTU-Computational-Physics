import numpy as np
import matplotlib.pyplot as plt

#grid number on half space (without the origin)
N=150
#total grid number = 2*N + 1 (with origin)
N_g=2*N+1
#finite barrier potential value = 300 (meV)
potential_value=300

#building potential:
def potential(potential_value):
    V=np.zeros((1,N_g),dtype=float)
    V[0,0:100]=potential_value
    V[0,100:201]=0
    V[0,201:]=potential_value
    return V

# #Hamiltonian matrix:
def Hamiltonian(V):
    H=np.zeros((N_g,N_g),dtype=float)
    dx=10 #0.1 (nanometer)
    for i in range(0,N_g):
        for  j in range(0,N_g):
            if i==j:
                x=dx*(i-N) #position
                H[i,j]=1/(dx**2)+V[0,i]
            elif j==i-1 or j==i+1:
                H[i,j]=-0.5/(dx**2)
    return H

V=potential(potential_value)
H=Hamiltonian(V)

eigenvalue,eigenvector=np.linalg.eig(H)
idx=np.argsort(eigenvalue)
eigenvalue=eigenvalue[idx]
eigenvector=eigenvector[:,idx]

fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(121)
x=np.linspace(0,10,11)
ax1.plot(x,eigenvalue[0:11],'r.',label='numerical')
ax1.set_xlabel('n')
ax1.set_ylabel('$E_n$')
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
ax2.plot(x,V.reshape(301,),label='potential')
ax2.set_xlabel('position (x)')
ax2.set_ylabel('wave function square')
ax2.set_title('The probability of the lowest eigen state')
ax2.set_ylim(0,0.03)
ax2.set_xlim(-1.75,1.75)
ax2.legend()
ax2.grid(True)
plt.show()
