import numpy as np
import matplotlib.pyplot as plt

N=51
x=np.linspace(0,5,N)
y_ana=1-np.exp(-x)

plt.plot(x,y_ana,label="v")
plt.title("Falling object in a fluid")
plt.legend()
plt.show()

