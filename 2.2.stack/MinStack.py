class MinStack:   

    def __init__(self): 
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return(self.stack[-1])

    def getMin(self) -> int:
        return(sorted(self.stack)[0]) 
    
ob = MinStack()

ob.push(2)
ob.push(-3)
ob.push(1)
assert ob.top() == 1
assert ob.getMin() == -3
ob.pop()
assert ob.top() == -3
ob.push(-5) 
assert ob.getMin() == -5
