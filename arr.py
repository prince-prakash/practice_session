from array import *
vals = array([5,6,8,2,3])
vals.reverse()
print(vals)
vals.reverse()
for i in range(len(vals)):     # Method 1
    print(vals[i], end=' ')
print()
for e in vals:                 # Method 2
    print(e, end=' ')
print()
for i in range(5):             # Method 3
    print(vals[i], end=' ')

newarr = array(vals.typecode, [a**2 for a in vals])
print(newarr)
