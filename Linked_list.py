import pdb
#create a new Node
class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next = next_node

#create the head of the linked list
class Linkedlist:
    def __init__(self):
        self.head = None

    #Insert Node at the end of the LL
    def insert(self,data):
        new_node = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    #Insert Node at specific location of LL
    def insertNodeAt(self,data,position):
        new_node = Node(data)
        current = self.head

        for i in range(1,position-1):
            current = current.next
        next = current.next
        current.next = new_node
        new_node.next = next

    #delete a Node from specific location of LL
    def deleteNodeAt(self,location):
        current = self.head
        for i in range(1,location-1):
            current = current.next
        current.next = current.next.next


    #print LL
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    '''printMiddleNode :: Idea : Initialized the temp variable as head
    Initialized count to Zero
    Take loop till head will become Null(i.e end of the list) and 
    increment the temp node when count is odd only, in this way 
    temp will traverse till mid element and head will traverse all
    linked list. Print the data of temp.'''
    def printMiddleNode(self):
        temp = current = self.head
        count = 0

        while current:
            if count%2 != 0:
                temp = temp.next
            count += 1
            current = current.next

        print("Middle element is {}".format(temp.data))


    def reverseLL(self):
        if self.head is None:
            return
        self.reverseUtils(self.head,None)

    def reverseUtils(self,curr,prev):

        #if current is the Tail of the LL
        if curr.next is None:
            self.head = curr

            #Update next of Current to prev
            curr.next = prev
            return

        #save the next of current for recursive call
        next = curr.next

        #Update the next
        curr.next = prev

        self.reverseUtils(next,curr)

#creating linked-list head and insert data in head.data
obj_linklist = Linkedlist()
obj_linklist.head = Node(1)
obj_linklist.insert(2)
obj_linklist.insert(3)
obj_linklist.insert(4)
obj_linklist.insert(5)
obj_linklist.insert(6)
obj_linklist.insert(7)
obj_linklist.printLL()
print("========================")
obj_linklist.printMiddleNode()
#pdb.set_trace()
#obj_linklist.reverseLL()
#obj_linklist.insertNodeAt(12,3)
#obj_linklist.printLL()


print(range(0,10))









