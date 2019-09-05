# To find odd and even number between the input range
num = int(input('Enter the number: '))
print('Even Values: ', end='')
for i in range(1, num):
    if i % 2 == 0:
        print(i, end=' ')
print()
print('Odd Values: ', end='')
for j in range(1, num):
    if j % 2 != 0:
        print(j, end=' ')

