print('Area of the triangle....')
a = int(input('Enter the first side: '))
b = int(input('Enter the second side: '))
c = int(input('Enter the third side: '))

s = (a+b+c)/2
print(s)
s1 = (s*(s-a)*(s-b)*(s-c))-(1/2)
print(s1)