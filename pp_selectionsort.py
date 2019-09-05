def selectionsort(list):
    l = len(list)
    new_list = []
    for i in range(l):
        mini = min(list)
        new_list.append(mini)
        list.remove(mini)

    for i in range(l):
        print(new_list[i], end=" ")


list = [5, 3, 1, 7, 6, 25, 90, 2]
selectionsort(list)