def primef(l, u=2):
        for i in range(u, l):
            for j in range(2, i):
                if i % j == 0:
                    j += 1
                    break
            else:
                print(i)
                i += 1

def smart_prime(func):
    def swap(a, b):
        a, b = b, a
        return func(a, b)
    return swap

user_in = input('Do you want to set both upper and lower limit Y/N: ')
if user_in == 'y':
    user1_in1 = input('Enter the Last Limit of the number: ')
    primef(int(user1_in1))
else:
    user1_in1 = input('Enter the Upper Limit: ')
    user1_in2 = input('Enter the Lower limit:')
    div1 = smart_prime(primef)
    print(div1(int(user1_in1), int(user1_in2)))
