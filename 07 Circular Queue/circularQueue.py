class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if ((self.rear+1) % self.size == self.front):
            print("Queue if full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size
    
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.dequeue()
cq.enqueue(6)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()