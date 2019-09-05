num = int(input('Enter the number for factorial'))
w = 1
if num < 0:
    print('Enter the correct positive Number!!!')
    exit(1)
else:
    global w
    for i in range(1, num+1):
        w = w * i

print(w)
