def bubblesort(list):
    l = len(list)
    for j in range(l):
        for i in range(l-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

    for i in range(l):
        print(list[i], end=" ")

list = [5,3,1,5,7,6,25,90,2,90]
bubblesort(list)
