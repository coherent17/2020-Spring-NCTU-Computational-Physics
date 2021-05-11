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

#sort the eigenvalue and get the corresponding eigenvector
eigenvalue,eigenvector=np.linalg.eig(H)
idx=np.argsort(eigenvalue)
eigenvalue=eigenvalue[idx]
eigenvector=eigenvector[:,idx]

#visualize
fig=plt.figure(figsize=(18,6))
ax1=fig.add_subplot(131)
x=np.linspace(0,10,11)
ax1.plot(x,eigenvalue[0:11],'r.',label='numerical')
ax1.set_xlabel('n')
ax1.set_ylabel('$E_n (meV)$')
ax1.set_title('eigen energies')
ax1.grid(True)
ax1.legend()

ax2=fig.add_subplot(132)
x=np.linspace(-5,5,301)
#x/lamda_0
x=x/(np.sqrt(2)*10**(10-9)/np.pi)
y1=eigenvector[:,0]
y2=eigenvector[:,1]
y3=eigenvector[:,2]
y4=eigenvector[:,3]
y5=eigenvector[:,4]
ax2.plot(x,(y1),label='$Ψ_{n=0}(x)$')
ax2.plot(x,(y2),label='$Ψ_{n=1}(x)$')
ax2.plot(x,(y3),label='$Ψ_{n=2}(x)$')
ax2.set_xlabel('position ($x/λ_0$) ')
ax2.set_ylabel('wavefunction')
ax2.set_title('wave function in different eigen state')
ax2.legend()
ax2.grid(True)

ax3=fig.add_subplot(133)
ax3.plot(x,(y1**2),label='$Ψ^2_{n=0}(x)$')
ax3.plot(x,(y2**2),label='$Ψ^2_{n=1}(x)$')
ax3.plot(x,(y3**2),label='$Ψ^2_{n=2}(x)$')
ax3.set_xlabel('position ($x/λ_0$) ')
ax3.set_ylabel('square wavefunction')
ax3.set_title('probability distribution in finite barrier well')
ax3.grid(True)
ax3.legend()
plt.show()