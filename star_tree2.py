hieght = eval(input("Enter the height of tree: "))
row = 0

while row < hieght:
    k = 0
    while k <= hieght - 1:
        print(end=' ')
        k += 1
    col = 0
    while col <= hieght-1:
        print('*', end='')
        col += 1
    row += 1
    print()

