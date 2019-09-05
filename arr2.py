from array import *

ar = array('i', [])
num = int(input("Enter the length of the array"))

for i in range(num):
    en = int(input("Enter the Number: "))
    ar.append(en)
print(ar)
ip  = int(input("Enter the number to be searched: "))
k = 0                                                           # Method 1
for i in ar:
    if i==ip:
        print(k)
        break
    k += 1

print(ar.index(ip))                                              # Method 2

from numpy import *

are = arange(0, 20, 5)
print(are)
are = linspace(0, 20)
print(are)

print(id(are))