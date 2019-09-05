class race:
    def __init__(self,ram):
        self.ram = ram
        print('This is Parameterized Constructor')
    def config(self):
        print("RAM: ",self.ram)

race = race("8GB")
race.config()



class race2:
    def __init__(self):
        print('This non -paramertized Constructor')
    def config(self,ram):
        print('RAM: ',ram)
race2 = race2()
race2.config('16GB')

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even = list(filter(lambda n: n % 2 == 0, num))
odd = list(filter(lambda n: n % 2 != 0, num))
print('Even = {} \nOdd = {}'.format(even, odd))