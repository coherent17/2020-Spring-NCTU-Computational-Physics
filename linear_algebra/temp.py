for i in range(1,9):

    #print the space
    for j in range(16-i):
        print(" ",end="")

    #print the star
    for j in range(2*i-1):
        print("*",end="")
    print("")

#middle part
for i in range(31):
    print("*",end="")
print("")

for i in range(0,5):

    #print the space bar
    for j in range(i+1):
        print(" ",end="")

    #print the star
    for j in range(29-2*i):
        print("*",end="")
    print("")

for i in range(1,6):
    
    #print the space bar
    for j in range(6-i):
        print(" ",end="")

    for j in range(9-2*(i-1)):
        print("*",end="")
    
    for j in range(2+6*(i-1)):
        print(" ",end="")

    for j in range(9-2*(i-1)):
        print("*",end="")
    print("")

