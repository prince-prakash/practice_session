class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def total(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        ele = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            ele.append(cur.data)
        print(ele)

    def delete(self, node):
        cur = self.head
        while True:
            last = cur
            cur = cur.next
            if cur.data == node:
                last.next = cur.next
                break

    def appendmid(self, data, pos):
        new_node = node(data)
        cur = self.head
        total = 0
        while True:
            temp = cur
            cur = cur.next
            total += 1
            if total == pos:
                break
        temp.next = new_node
        new_node.next = cur

    def removeduplicate(self):
        cur = self.head
        pre = None
        dictionary = dict()
        while cur:
            if cur.data in dictionary:
                pre.next = cur.next
            else:
                dictionary[cur.data] = 'Value'
                pre = cur
            cur = pre.next
        print(dictionary)

list1 = linkedlist()
list1.append(5)
list1.append(6)
list1.append(7)
print(list1.total())
list1.display()
list1.delete(6)
list1.display()
list1.appendmid(2, 2)
list1.append(8)
list1.append(8)
list1.removeduplicate()
list1.display()
