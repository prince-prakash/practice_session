def search(list, num):  ## Caution: Should have a sorted array
    u = 0
    l = len(list)
    mid = l//2
    while list[mid] < num or list[mid] > num:
        if list[mid] < num:
            u = mid + 1
        else:
            l = mid - 1
        mid = (u+l)//2

    print(mid+1)

list = [4, 6, 19, 20, 21, 56]
search(list, 70)
