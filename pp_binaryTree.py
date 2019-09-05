class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)



    def dele(self, data):
        if self.data:
            if self.data == data:
                print('Cannot delete but only be replaced')

                next = self.left
                while next.data != data:
                    if next.left:
                        next.left.trav()
                    if next.right:
                        next.right.trav()

    def indisplay(self):        #Inorder display
        if self.left:
            self.left.indisplay()
        print(self.data, end=" ")
        if self.right:
            self.right.indisplay()

    def predisplay(self):        #Preorder display
        print(self.data, end=" ")
        if self.left:
            self.left.predisplay()
        if self.right:
            self.right.predisplay()

    def postdisplay(self):        #Postorder display
        if self.left:
            self.left.postdisplay()
        if self.right:
            self.right.postdisplay()
        print(self.data, end=" ")

list = node(12)
list.insert(5)
list.insert(2)
list.insert(8)
list.insert(6)
list.insert(7)
list.insert(0)
list.insert(10)
print('Pre-Order')
list.predisplay()
print('\nIn-order')
list.indisplay()
print('\nPost-order')
list.postdisplay()
