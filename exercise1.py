import math 
#1-a
def function1():
    value=0
    for i in range(1,1000+1):
        value+=i
    return value

#1-b
def function2(m):
    value=0
    for i in range(1,m+1):
        value+=i
    return value
#2
def function3():
    value=0
    for i in range(1,100+1):
        value+=math.sqrt(i*math.pi/100)*math.sin(i*math.pi/100)
    return value

print(function1())
print(function2(1000))
print(function3())