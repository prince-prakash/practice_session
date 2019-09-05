from pp_stack import stack
def binary_stack(num):

    s = stack()
    l = bin(num)
    for i in range(len(l)):
        s.push(l[i])
    print(s.get_stack())
    print(s.pop())

r = binary_stack(242)

