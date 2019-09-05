class node:
    def __init__(self, data=None):
        self.data = data
        self.pre = None
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
        new_node.pre = cur


    def display(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data, end=' ')

    def appendmid(self, data, pos):
        new_node = node(data)
        cur = self.head
        total = 0
        while True:
            cur = cur.next
            total += 1
            if total == pos:
                break
        new_node.next = cur.next
        new_node.pre = cur
        cur.next = new_node


    def dele(self, data):
        cur = self.head
        while True:
            temp = cur
            cur = cur.next
            if cur.data == data:
                break

        temp.next = cur.next     # Satisfying previous and next nodes for after deletion
        cur = temp.next
        cur.pre = temp


list1 = linkedlist()
list1.append(1)
list1.append(2)
list1.append(3)
list1.display()
print()
list1.appendmid(4,3)
list1.appendmid(5,4)
list1.display()
print()
list1.dele(4)
list1.display()