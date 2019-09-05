class simplequeue:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def display(self):
        l = len(self.list)
        for i in range(l):
            print(self.list[i], end=' ')
        print()

    def dele(self,data):
        l = len(self.list)
        for i in range(l-1):
            if self.list[i] == data:
                self.list.pop(i)

class priorityqueue:
    def __init__(self):
        self.list = []
        self.l = 0
    def push(self, data, pos=None):
        self.l = 0
        while True:
            self.l += 1
            if pos != None and self.l == pos:
                self.list.append(data)
                break
            else:
                self.list.append(data)
                break

    def display(self):
        l = len(self.list)
        for i in range(l):
            print(self.list[i], end=' ')
        print()

    def dele(self, data):
        l = len(self.list)
        for i in range(l-1):
            if self.list[i] == data:
                self.list.pop(i)



qlist = priorityqueue()
qlist.push(1)
qlist.push(2)
qlist.push(3)

qlist.display()
qlist.push(4,2)
qlist.dele(2)
qlist.display()