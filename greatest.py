def compare(num, nu1):
    if num > nu1:
        return num
    else:
        return nu1


num = input("Enter the First number: ")
num1 = input("Enter the Second number: ")
num2 = input("Enter the Third number: ")
w = compare(num, num1)
if w < num2:
    print(num2)
else:
    print(w)
