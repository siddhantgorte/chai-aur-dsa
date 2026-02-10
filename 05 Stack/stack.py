class stack:
    def __init__(self):
        self.s = []
    
    def lengthOfStack(self):
        return len(self.s)
    
    def pushStack(self, value):
        self.s.insert(0, value)

    def topOfStack(self):
        if len(self.s) == 0:
            raise Exception('Stack is empty')
        else:
            return self.s[0]
    
    def popStack(self):
        if len(self.s) == 0:
            raise Exception('Stack is empty')
        else:
            return self.s.pop(0)

stk = stack()
stk.pushStack(10)
stk.pushStack(20)
stk.pushStack(30)
print(stk.topOfStack())
print(stk.popStack())
print(stk.popStack())
print(stk.popStack())


