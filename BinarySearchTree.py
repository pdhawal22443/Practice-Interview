class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self,data):
        if self.data :
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = Node(data)

    def printTreeInorder(self):
        if self.left:
            Node.printTreeInorder(self.left)
        print(self.data)
        if self.right:
            Node.printTreeInorder(self.right)


obj = Node(10)
obj.insert(6)
obj.insert(12)
obj.insert(14)
obj.insert(5)

obj.printTreeInorder()