import math
import random

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

d = (b**2)-(4*a*c)
sol1 = (-b+math.sqrt(d))/(2*a)
sol2 = (-b-math.sqrt(d))/(2*a)

print(sol1, sol2)

r = random.randint(100, 500)
print(r)