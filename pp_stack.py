class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def top(self):
        return self.items[-1]

    def empty(self):
        for i in range(len(self.items)):
            self.items.pop()



'''s = stack()
s.push('A')
s.push('B')
s.push('C')
s.push('D')
s.push('E')
print(s.get_stack())
print(s.top())
s.pop()
print(s.get_stack())
s.empty()
print(s.get_stack())'''