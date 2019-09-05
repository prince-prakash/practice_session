def insertionsort(list):
    l = len(list)
    for i in range(l):
        for i in range(l-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

    for i in range(l):
        print(list[i], end=' ')

list = [5, 3, 1, 7, 25, 90, 2]
insertionsort(list)
