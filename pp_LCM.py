def lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if(greater%x == 0) and (greater%y == 0):
            lcm = greater 
            break
        greater += 1
    return lcm

num = int(input('Enter the first number '))
num1 = int(input('Enter the seccond value '))
print('LCM for {} and {} is {}'.format(num,num1,lcm(num,num1)))