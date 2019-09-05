decision = input('Traditional or Easy method (Type T or E): ')
if decision == 'T':
    num1 = int(input('Enter the first number:'))
    num2 = int(input('Enter the second number'))
    cal = input('Enter [add],[mul],[div],[sub]: ')

    if cal == 'add':
        add = num1 + num2
        print('Answer {}'.format(add))
    elif cal == 'sub':
        sub = num1 - num2
        print('Answer {}'.format(sub))
    elif cal == 'mul':
        mul = num1 * num2
        print('Answer {}'.format(mul))
    elif cal == 'div':
        div = num1 / num2
        print('Answer {}'.format(div))
    else:
        print('Please restart and enter the specific function!!!!!')

elif decision == 'E':
    num = eval(input('Enter the number with the function specific: '))
    print(num)
else:
    print('there is a missing input please restart!!!')