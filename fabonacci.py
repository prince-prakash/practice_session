import sys
w = eval(sys.argv[1])  # Only used in command prompt
i = m = 1
r = x = 0

while i < w:
    print(x, end=" ")
    r = x + m
    x = m
    m = r
    i += 1
ra = 2
print("\nPrime Values: ")
while ra <= w:
    flag = 1
    fact = 2
    while fact < ra:
        if ra % fact == 0:
            flag = 2
            break
        fact += 1
    if flag == 1:
        print(fact, end=" ")
    ra += 1


