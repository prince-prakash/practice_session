def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m-n)
    print(res)

g(47,7)