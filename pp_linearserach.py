def search(list, num):
    for i in range(len(list)):
        if list[i] == num:
            print(num, i+1)
    else:
        print('Not In the list')

list = [4, 6, 19, 20, 21, 56]
search(list, 70)
