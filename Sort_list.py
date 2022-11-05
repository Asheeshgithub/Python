import numpy as np
import sys

#b=[]
a = input("enter length of list :")
b=list(input("enter list value: ") for i in range(int(a)+1))
print(b)
l = len(b)


while(l>=0):
    for y in range(l-1):
        
        if b[y] > b[y+1]:
            aux = b[y]
            b[y] = b[y+1]
            b[y+1] = aux
            
        else:
             pass
    l = l-1

print("sorted list:",b)
print("second highest number: ", b[1])
