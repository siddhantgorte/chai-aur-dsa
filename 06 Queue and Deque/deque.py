class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtStart(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)
        
    def insertAtStart(self, value):
        self.items.insert(0, value)

    def deleteAtEnd(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop()
    
dq = Deque()
dq.insertAtEnd(10)
dq.insertAtStart(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtStart(50)
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtStart())
print(dq.deleteAtStart())
print(dq.deleteAtEnd())
dq.deleteAtEnd()
dq.deleteAtStart()