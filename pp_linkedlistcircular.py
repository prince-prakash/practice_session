class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.pre = None

class linkedlist():

    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        cur.next = new_node
        new_node.pre = cur
        new_node.next = self.head


    def display(self):
        cur = self.head
        temp = cur
        while True:
            cur = cur.next
            print(cur.data, end=' ')
            if cur == temp:
                break

    def dele(self, data):
        cur = self.head
        while True:
            temp = cur
            cur = cur.next
            if cur.data == data:
                break
        temp.next = cur.next
        cur.next = temp

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



list1 = linkedlist()
list1.append(1)
list1.append(2)
list1.append(3)
list1.display()