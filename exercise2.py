import numpy as np

#solve (x_1)+4*(x_2)=2,-2*(x_1)+x_2=14
A=np.array([[1,4]
           ,[-2,1]])

print("det(A)=",np.linalg.det(A))
#det(A)= 9.000000000000002
#the reason that 2 appear here:
#the decimal calcuation error
#det(A)!=0 -> not singular matrix
# -> has unique solution

b=np.array([2,14])
x=np.linalg.solve(A,b)
print(x)
#[-6.  2.]

class Uniqueness_of_solution:
    def __init__(self):
        pass
    def judge_solution(self,A,b):
        #to avoid the decimal error
        #determine by the value of the det(A)by a small float number
        if abs(np.linalg.det(A))<0.0000001:
            print("doesn't have a unique solution")
        else:
            print("has a unique solution:")
            print(np.linalg.solve(A,b))
            return np.linalg.solve(A,b)


#solve:
#x-4y+6z=3
#-2x+8y-12z=-6
#2x-y+3z=1

C=np.array([[1,-4,6]
           ,[-2,8,-12]
           ,[2,-1,3]])

D=np.array([3,-6,1])

sol=Uniqueness_of_solution()
sol.judge_solution(A,b)
#[-6.  2.]
sol.judge_solution(C,D)
#doesn't have a unique solution

#What if doesn't have a unique solution and using linalg.solve?
# ans=np.linalg.solve(C,D)
# print(ans)
#terminal:
#numpy.linalg.LinAlgError: Singular matrix


#solve for the traffic flows
# (x_1)-(x_2)=160
# (x_2)-(x_3)=-40
# (x_3)-(x_4)=210
# (x_4)-(x_1)=-330

E=np.array([[1,-1,0,0]
           ,[0,1,-1,0]
           ,[0,0,1,-1]
           ,[-1,0,0,1]])

F=np.array([160,-40,210,-330])

print("det(E)=",np.linalg.det(E))
if np.linalg.det(E)!=0:
    print("non-singular matrix")
else:
    print("singular matrix")
# det(E)= 0.0
# singular matrix

#solve for the traffic flows (if (x_4)=100)

G=np.array([[1,0,0]
           ,[1,-1,0]
           ,[0,0,1]])

H=np.array([430,160,310])

print("det(G)=",np.linalg.det(G))
if np.linalg.det(G)!=0:
    print("non-singular matrix")
    print("the solution is:")
    print(np.linalg.solve(G,H))
else:
    print("singular matrix")

# det(G)= -1.0
# non-singular matrix
# the solution is:
# [430. 270. 310.]