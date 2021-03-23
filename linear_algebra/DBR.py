import numpy as np
import matplotlib.pyplot as plt
import cmath 

D_1=np.array([[1+0j,1+0j]
               ,[2.35+0j,-2.35+0j]])

D_2=np.array([[1+0j,1+0j]
               ,[1.38+0j,-1.38+0j]])

lam=350
d1=550/(4*2.35)
d2=550/(4*1.38)
phi1=2.35*(2*cmath.pi*d1/lam)+0j
phi2=1.38*(2*cmath.pi*d2/lam)+0j

P_1=np.array([[cmath.exp(-1j*phi1),0+0j]
               ,[0+0j,cmath.exp(1j*phi1)]])

P_2=np.array([[cmath.exp(-1j*phi2),0]
               ,[0,cmath.exp(1j*phi2)]])

M=np.matmul(np.matmul(np.matmul(np.matmul(np.matmul(np.linalg.pinv(D_1),D_2),P_2),np.linalg.pinv(D_2)),D_1),P_1)

M=np.matmul(M,M)
print(M)

