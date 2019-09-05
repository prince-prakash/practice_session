hieght = int(input("Enter the height of tree: "))
row = 0

while row <= hieght:
    col = 1
    while col <= row:
        print(col, end=' ')
        col += 1
    row += 1
    print()