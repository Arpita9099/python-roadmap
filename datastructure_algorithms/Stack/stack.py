# from collections import deque

# class Stack:
#     def __init__(self):
#         self.stk = deque()

# if __name__ == "__main__":
#     ob = Stack()

from collections import deque

class Stack:
    def __init__(self):
        self.stk = deque()

    def is_empty(self):
        return len(self.stk) == 0
    
    def push(self, elm):
        self.stk.append(elm)

    def pop(self):
        return self.stk.pop()
    
    def reverse_string(self, s):
        rstr = ""
        for ch in s:
            ob.push(ch)
        while not ob.is_empty():
            rstr = rstr + ob.pop()
        return rstr
    
if __name__ == "__main__":
    ob = Stack()
    print(ob.reverse_string("We will conquere COVID-19"))

