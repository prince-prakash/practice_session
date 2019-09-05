def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

def selsort(num):
    for i in range(len(num)):
        minpos = i
        for j in range(i, len(num)-i):
            if num[j] < num[minpos]:
                minpos = j
        num[i], num[minpos] = num[minpos], num[i]

num = [5,3,8,6,7,2]
sort(num)
print(num)
selsort(num)
print(num)

