import random
def mergesort(list):
    new_list = []
    new_list1 = []
    new_list2 = []
    l = len(list)
    mid = random.randint(0, l)
    left_list = list[:mid]
    right_list = list[mid:]

    for i in range(len(left_list)):
        mini = min(left_list)
        new_list.append(mini)
        left_list.remove(mini)

    for i in range(len(right_list)):
        mini = min(right_list)
        new_list1.append(mini)
        right_list.remove(mini)

    res = new_list + new_list1
    for i in range(l):
        mini = min(res)
        new_list2.append(mini)
        res.remove(mini)

    for i in range(l):
        print(new_list2[i], end=' ')


list = [5, 3, 1, 7, 25, 90, 2]
mergesort(list)
