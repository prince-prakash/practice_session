class school:
    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu
        self.lap = self.laptop()
    def show(self):
        print(self.ram, self.cpu)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.ram = '8GB'
            self.cpu = 'i5'
        def show(self):
            print(self.ram, self.cpu)


sch = school('16GB', 'i7')
sch.show()



def div(a,b):
    return a/b

def smart(funct):
    def inner(a, b):
        a, b = b, a
        return funct(a, b)
    return inner

div1 = smart(div)
print(div1(2, 4))
print('run off')