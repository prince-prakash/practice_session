r = eval(input("Enter the Number: "))
count = 1
while count <= r:
    m = 0
    while m < count:
        print("*", end=" ")
        m += 1
    print("")
    count += 1