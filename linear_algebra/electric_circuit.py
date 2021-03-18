import numpy as np

#note that the datatype of the matrix should be float
#or the element during GE may be wrong

#original
A=np.float64([[1,-1,1]
             ,[-1,1,-1]
             ,[4,2,0]
             ,[0,2,5]])

B=np.float64([[0]
             ,[0]
             ,[8]
             ,[9]])

#if there is any row filling with 0 
#delete it
def del_zero(A,B):
    zero_row=[]
    for i in range(0,len(A)):
        flag=0
        for j in range(0,np.shape(A)[1]):
            if A[i,j]==0:
                flag+=1
        if flag==np.shape(A)[1]:
            zero_row.append(i)
    A=np.delete(A,zero_row,axis=0)
    B=np.delete(B,zero_row,axis=0)
    return A,B

def change_row(A,B):
    if A[0,0]==0:
        temp=A[0,:]
        temp1=B[0]
        A=np.delete(A,0,axis=0)
        A=np.insert(A,[1],temp,axis=0)
        B=np.delete(B,0,axis=0)
        B=np.insert(B,[1],temp1,axis=0)
    return A,B


def GE(A,B):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[j,i]!=0:
                lam=A[j,i]/A[i,i]
                A[j,:]=A[j,:]-lam*A[i,:]
                B[j]=B[j]-lam*B[i]
                A,B=del_zero(A,B)
                break
        else:
            continue
        break
        
    print(np.c_[A,B],"\n")
    return A,B

#back substitution
def BS(A,B):
    sol=np.zeros((len(A)))
    sol[len(A)-1]=B[len(A)-1]/A[len(A)-1,len(A)-1]

    for i in range(len(A)-2,-1,-1):
        sol[i]=(B[i]-np.dot(A[i,i+1:len(A)],sol[i+1:len(A)]))/A[i,i]
    # sol[1]=(B[1]-A[1,2]*sol[2])/A[1,1]
    # sol[0]=(B[0]-A[0,2]*sol[2]-A[0,1]*sol[1])/A[0,0]
    for j in range(0,len(A)):
        print("i_",j+1,"=",sol[j],end="   ")
    print("\n")

#avoid the original A matrix has invalid value
A,B=del_zero(A,B)

#keep doing GE until the matrix are all the same
def GE_BS(A,B):
    #check if A[0,0]==0 if yew -> change the row
    A,B=change_row(A,B)
    for _ in range(1000):
        A,B=GE(A,B)
        C=np.c_[A,B]
        A,B=GE(A,B)
        D=np.c_[A,B]
        if np.all((C==D)):
            break
    BS(A,B)

GE_BS(A,B)
#result:
# [[ 1. -1.  1.  0.] 
#  [ 4.  2.  0.  8.] 
#  [ 0.  2.  5.  9.]]

# [[ 1. -1.  1.  0.]
#  [ 0.  6. -4.  8.]
#  [ 0.  2.  5.  9.]]

# [[ 1.         -1.          1.          0.        ]
#  [ 0.          6.         -4.          8.        ]
#  [ 0.          0.          6.33333333  6.33333333]]

# [[ 1.         -1.          1.          0.        ]
#  [ 0.          6.         -4.          8.        ]
#  [ 0.          0.          6.33333333  6.33333333]]

# i_ 1 = 0.9999999999999998   i_ 2 = 2.0   i_ 3 = 1.0000000000000002



#note that there might be a little bit wrong to the right answer
#because lambda can't be divided

#now we change the sequence of the original array test whether the solution are the same

#original
# A=np.float64([[1,-1,1]
#              ,[-1,1,-1]
#              ,[4,2,0]
#              ,[0,2,5]])

# B=np.float64([[0]
#              ,[0]
#              ,[8]
#              ,[9]])

#testing matrix change the 3 and 4 row can it get the same value?
C=np.float64([[1,-1,1]
             ,[-1,1,-1]
             ,[0,2,5]
             ,[4,2,0]])

D=np.float64([[0]
             ,[0]
             ,[9]
             ,[8]])

GE_BS(C,D)
#result:
# [[ 1. -1.  1.  0.]
#  [ 0.  2.  5.  9.]
#  [ 4.  2.  0.  8.]]

# [[ 1. -1.  1.  0.]
#  [ 0.  2.  5.  9.]
#  [ 0.  6. -4.  8.]]

# [[  1.  -1.   1.   0.]
#  [  0.   2.   5.   9.]
#  [  0.   0. -19. -19.]]

# [[  1.  -1.   1.   0.]
#  [  0.   2.   5.   9.]
#  [  0.   0. -19. -19.]]

# i_ 1 = 1.0   i_ 2 = 2.0   i_ 3 = 1.0

#testing matrix change the 2 and 3 row can it get the same value?
#original
# A=np.float64([[1,-1,1]
#              ,[-1,1,-1]
#              ,[4,2,0]
#              ,[0,2,5]])

# B=np.float64([[0]
#              ,[0]
#              ,[8]
#              ,[9]])

E=np.float64([[1,-1,1]
             ,[4,2,0]
             ,[-1,1,-1]
             ,[0,2,5]])

F=np.float64([[0]
             ,[8]
             ,[0]
             ,[9]])

GE_BS(E,F)
#results
# [[ 1. -1.  1.  0.]
#  [ 0.  6. -4.  8.]
#  [-1.  1. -1.  0.]
#  [ 0.  2.  5.  9.]]

# [[ 1. -1.  1.  0.]
#  [ 0.  6. -4.  8.]
#  [ 0.  2.  5.  9.]]


# [[ 1.         -1.          1.          0.        ]
#  [ 0.          6.         -4.          8.        ]
#  [ 0.          0.          6.33333333  6.33333333]]

# [[ 1.         -1.          1.          0.        ]
#  [ 0.          6.         -4.          8.        ]
#  [ 0.          0.          6.33333333  6.33333333]]

# i_ 1 = 0.9999999999999998   i_ 2 = 2.0   i_ 3 = 1.0000000000000002

#test if A[0,0]==0, will the change_row function run?
#original
# A=np.float64([[1,-1,1]
#              ,[-1,1,-1]
#              ,[4,2,0]
#              ,[0,2,5]])

# B=np.float64([[0]
#              ,[0]
#              ,[8]
#              ,[9]])

#change the 1 and 4 row
G=np.float64([[0,2,5]
             ,[-1,1,-1]
             ,[4,2,0]
             ,[1,-1,1]])

H=np.float64([[9]
             ,[0]
             ,[8]
             ,[0]])


GE_BS(G,H)
#results:
# [[-1.  1. -1.  0.]
#  [ 0.  2.  5.  9.]
#  [ 0.  6. -4.  8.]
#  [ 1. -1.  1.  0.]]

# [[-1.  1. -1.  0.]
#  [ 0.  2.  5.  9.]
#  [ 0.  6. -4.  8.]]

# [[ -1.   1.  -1.   0.]
#  [  0.   2.   5.   9.]
#  [  0.   0. -19. -19.]] 

# [[ -1.   1.  -1.   0.]
#  [  0.   2.   5.   9.]
#  [  0.   0. -19. -19.]]

# i_ 1 = 1.0   i_ 2 = 2.0   i_ 3 = 1.0