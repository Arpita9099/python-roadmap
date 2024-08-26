from collections import deque

class Parantheses:
    def __init__(self):
        self.stk = deque()
        self.d = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

    def push(self, elm):
        self.stk.append(elm)

    def pop(self):
        return self.stk.pop()
    
    def is_balanced(self, s):
        for ch in s:
            if ch in self.d.keys():
                self.push(ch)
            elif ch in self.d.values():
                if self.stk and self.d[self.stk[-1]] == ch:
                    self.pop()
                else: 
                    return False
        return  not self.stk # len(self.stk) == 0

if __name__ == "__main__":
    ob = Parantheses()
    print(ob.is_balanced("({a+b})"))
    print(ob.is_balanced("))((a+b}{"))
    print(ob.is_balanced("((a+b))"))
    print(ob.is_balanced("))"))
    print(ob.is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    print(ob.is_balanced("}"))