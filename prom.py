r = int(input("Enter the number: "))
for num in range(r+1):
    for i in range(2,num):
        if num % i == 0:
            break
        else:
            print(num)
            break
