class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, value):
        temp = Node(value)
        
        if self.head == None:
            self.head = temp
            return
        
        t = self.head
        while t.next != None:
            t = t.next
        
        t.next = temp
        temp.prev = t

    def insertAtStart(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
            return
        
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMiddle(self, value, x):
        t = self.head

        while t.next != None:
            if t.data == x:
                break
            else:
                t = t.next
        
        temp = Node(value)
        temp.next = t.next
        temp.next.prev = temp
        temp.prev = t
        t.next = temp
    
    def deleteNode(self, value):
        if self.head == value:
            self.head = None
            print('DLL is empty')
            return
        
        t = self.head

        #   Deletion from the start
        if t.data == value:
            self.head = t.next
            self.head.prev = None
            return
        
        #   Deletion from the middle
        while t.next != None:
            if t.data == value:
                t.next.prev = t.prev
                t.prev.next = t.next
                return
            t = t.next
        
        #Delete from the end
        if t.data == value:
            t.prev.next = None

    def printDll(self):
        t1 = self.head
        while t1.next != None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)

dll = Dll()
dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtEnd(30)
dll.insertAtEnd(40)
dll.insertAtStart(5)
dll.insertAtMiddle(9, 5)
dll.deleteNode(40)
dll.insertAtEnd(50)
dll.printDll()