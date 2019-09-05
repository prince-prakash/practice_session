i = eval(input("Enter the first number: "))
nos = eval(input("Enter the end number: "))
if i < 2:
    print("Please enter the first number more than 1!!!!")
else:
    while i <= nos:
        flag = 2
        factor = 2
        while factor < i:
            if i % factor == 0:
                flag = 1
                break
            factor += 1
        if flag == 2:
            print(factor, end=' ')
        i += 1