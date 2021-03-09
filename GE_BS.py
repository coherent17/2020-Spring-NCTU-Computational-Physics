import numpy as np
import math as m

class GE_BS():
    def __init__(self):
        pass

    def judge_solution(self,A,B):
        #infinite solution or no solution (detA==0)
        if abs(np.linalg.det(A))<0.000000000001:
            for i in range(0,len(A)):
                for j in range(i+1,len(A)):
                    #temp1:store the row_i/row_j
                    #temp2=B[i]/B[j]
                    temp1=[0]*len(A)
                    temp2=[0]
                    flag=0
                    count_infinite=0
                    count_no=0
                    for k in range(0,len(A)):
                        #here may be some problem:
                            #the division error
                        temp1[k]=A[i,k]/A[j,k]
                    temp2=B[i]/B[j]

                    #count how many number of the coeff is the same
                    for i in range(0,len(A)-1):
                        if temp1[i]-temp1[i+1]<0.000000001:
                            flag+=1

                    #if the flag number is equal to len(A):
                    #check for the B[i]/B[j] to judge whether infinite or no solution
                    if flag==len(A)-1 and abs(temp1[0]-temp2)<0.000000001:
                        count_infinite+=1
                    elif flag==len(A)-1 and (temp1[0]!=temp2):
                        count_no+=1
            if count_no>=1:
                print("there is no solution")
            else:
                print("there are infinite solutions")
                print("need more information")            

        #unique solution
        else:
            print("the matrix has a unique solution")

    #Gaussian Elimination
    def GE(self,A,B):
        for k in range(0,len(A)):
            for j in range(k+1,len(A)):
                if A[j,k]!=0:
                    lam=A[j,k]/A[k,k]
                    A[j,:]=A[j,:]-lam*A[k,:]
                    B[j]=B[j]-lam*B[k]
                    #per iteration print the whole matrix
                    print(np.c_[A,B])
        return A,B

    #BS for traffic flow
    def BS_for_traffic_flow(self,A,B):
        sol=np.zeros((len(A)))
        #x_4=100
        sol[3]=100
        for i in range(2,-1,-1):
            sol[i]=(B[i]-A[i,i+1]*sol[i+1])/A[i,i]
        
        for j in range(0,len(A)):
            print("x_",j,"=",sol[j],end="   ")

    def BS(self,A,B):
        pass

A=np.array([[1,-1,0,0]
           ,[0,1,-1,0]
           ,[0,0,1,-1]
           ,[-1,0,0,1]])

B=np.array([[160]
           ,[-40]
           ,[210]
           ,[-330]])  

sol=GE_BS()
A,B=sol.GE(A,B)
sol.BS_for_traffic_flow(A,B)
# [[   1   -1    0    0  160]
#  [   0    1   -1    0  -40]
#  [   0    0    1   -1  210]
#  [   0   -1    0    1 -170]]
# [[   1   -1    0    0  160]
#  [   0    1   -1    0  -40]
#  [   0    0    1   -1  210]
#  [   0    0   -1    1 -210]]
# [[  1  -1   0   0 160]
#  [  0   1  -1   0 -40]
#  [  0   0   1  -1 210]
#  [  0   0   0   0   0]]
# x_ 0 = 430.0   x_ 1 = 270.0   x_ 2 = 310.0   x_ 3 = 100.0