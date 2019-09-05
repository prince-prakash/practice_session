hieght = eval(input("Enter the height of tree: "))
row = 0
while row < hieght:
    count = 0
    while count < hieght - row:
        print(end='')
        count += 1
    count = 0
    while count< 2* row + 1:
        print(end=" ")
        count += 1
    print()
    row += 1
