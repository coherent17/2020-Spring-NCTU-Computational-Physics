import numpy as np
import matplotlib.pyplot as plt

A=np.array([[0.7,0.2]
          ,[0.3,0.8]])

B=np.array([[8000]
          ,[2000]])

year=10
married=[B[0,0]]
single=[B[1,0]]
for i in range(year):
    temp=np.matmul(A,B)
    B=temp
    married.append(B[0,0])
    single.append(B[1,0])

#visualize
x=np.arange(year+1)
plt.plot(x,married,color='blue',lw=1.0,ls='-',label="married")
plt.plot(x,single,color='red',lw=1.0,ls='-',label="single")
plt.xlabel("year")
plt.ylabel("number of people")
plt.title("martial population")
plt.legend()
plt.show()
