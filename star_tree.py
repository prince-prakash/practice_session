# Start Version
hieght = int(input("Enter the height of tree: "))
row = 0

while row < hieght:
    col = 0
    while col < row:
        print('*', end=' ')
        col += 1
    row += 1
    print()
row = 0
while row < hieght:
    col = 0
    while col < hieght - row:
        print('*', end=' ')
        col += 1
    row += 1
    print()

# Version 0.1
# This function is using concatination process because of the string type input to reduce code lines

num = '* '
for i in range(hieght+1):
    w = i * num
    print(w)
j = 4
while j < hieght:
    w = j * num
    print(w)
    if j == 0:
        break
    else:
        j = j - 1