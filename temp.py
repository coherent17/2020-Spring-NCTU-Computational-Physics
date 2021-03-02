a="abcdefghi"
b=[]
for i in range(len(a),0,-1):
    b.append(a[i-1])

for i in range(len(b)):
    print(b[i],end="")

import numpy as np
c=a.reverse
