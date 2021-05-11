import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermval
x=np.linspace(-3,3,1001)
def Hermite(n):
    matrix=np.zeros((n+1,))
    matrix[n]=1
    return hermval(x,matrix)
H_0=Hermite(0)
H_1=Hermite(1)
H_2=Hermite(2)
H_3=Hermite(3)
H_4=Hermite(4)
print(np.shape([0,1]))
plt.plot(x,H_0,label='$H_0$')
plt.plot(x,H_1,label='$H_1$')
plt.plot(x,H_2,label='$H_2$')
plt.plot(x,H_3,label='$H_3$')
plt.plot(x,H_4,label='$H_4$')
plt.xlabel('$x$')
plt.ylabel('$H_n(ξ)$')
plt.title('Hermite Polynomials,$H_n(ξ)$')
plt.xlim(-2.5,2.5)
plt.ylim(-20,20)
plt.legend()
plt.show()