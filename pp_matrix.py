num = [2, 3, 4], [5, 6, 7]
num2 = [8, 9, 10], [11, 12, 13]
num3 = [0, 0, 0], [0, 0, 0]
for i in range(len(num)):
    print(num[i])
for i in range(len(num)):
    print(num2[i])
print()
for i in range (len(num)):
    for j in range(len(num)+1):
        num3[i][j] = num[i][j] + num2[i][j]

for i in range(len(num3)):
    print(num3[i])