import numpy as np

#GE and BS

#GE
A=np.array([[1,-1,0,0]
           ,[0,1,-1,0]
           ,[0,0,1,-1]
           ,[-1,0,0,1]])

B=np.array([[160]
           ,[-40]
           ,[210]
           ,[-330]])

#k=0,j=1,pass
#k=0,j=2,pass
#k=0,j=3
lam=A[3,0]/A[0,0]
A[3,:]=A[3,:]-lam*A[0,:]
B[3]=B[3]-lam*B[0]

print(np.c_[A,B])
# [[   1   -1    0    0  160]
#  [   0    1   -1    0  -40]
#  [   0    0    1   -1  210]
#  [   0   -1    0    1 -170]]

#k=1,j=3
lam=A[3,1]/A[1,1]
A[3,:]=A[3,:]-lam*A[1,:]
B[3]=B[3]-lam*B[1]

print(np.c_[A,B])
# [[   1   -1    0    0  160]
#  [   0    1   -1    0  -40]
#  [   0    0    1   -1  210]
#  [   0    0   -1    1 -210]]

#k=2,j=3
lam=A[3,2]/A[2,2]
A[3,:]=A[3,:]-lam*A[2,:]
B[3]=B[3]-lam*B[2]

print(np.c_[A,B])
# [[  1  -1   0   0  160]
#  [  0   1  -1   0  -40]
#  [  0   0   1  -1  210]
#  [  0   0   0   0    0]]


A=np.array([[1,-1,0,0]
           ,[0,1,-1,0]
           ,[0,0,1,-1]
           ,[-1,0,0,1]])

B=np.array([[160]
           ,[-40]
           ,[210]
           ,[-330]])

def GE(A,B):
    for k in range(0,len(A)):
        for j in range(k+1,len(A)):
            if A[j,k]!=0:
                lam=A[j,k]/A[k,k]
                A[j,:]=A[j,:]-lam*A[k,:]
                B[j]=B[j]-lam*B[k]
                print(np.c_[A,B])
    return A,B,np.c_[A,B]

A=np.array([[1,-1,0,0]
           ,[0,1,-1,0]
           ,[0,0,1,-1]
           ,[-1,0,0,1]])

B=np.array([[160]
           ,[-40]
           ,[210]
           ,[-330]])    

A,B,total=GE(A,B)
# [[  1  -1   0   0 160]
#  [  0   1  -1   0 -40]
#  [  0   0   1  -1 210]
#  [  0   0   0   0   0]]


#BS
sol=np.zeros((len(A)))
#x_4=100
sol[3]=100
sol[2]=(B[2]-A[2,3]*sol[3])/A[2,2]
sol[1]=(B[1]-A[1,2]*sol[2])/A[1,1]
sol[0]=(B[0]-A[0,1]*sol[1])/A[0,0]
print("x_0=",sol[0])
print("x_1=",sol[1])
print("x_2=",sol[2])
print("x_3=",sol[3])

# def BS(A,B):
#     if A[len(A)-1,len(A)-1]==0:
#         print("you need to give me more value to solve the equation")
#     else:
               