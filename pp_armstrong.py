num = int(input('Enter the number'))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit**3
    temp //= 10

if total == num:
    print('This is fabonscci')
else:
    print('This is not fabonaaci')

### Armstrong number between the limit #######

lower = int(input('Enter the lower number'))
upper = int(input('Enter the upper limit'))

for num in range(lower, upper+1):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
        if num == total:
            print(num)