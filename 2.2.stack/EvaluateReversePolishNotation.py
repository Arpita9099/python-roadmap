class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(i))
                
        return(stack[0])
    
ob = Solution()

assert ob.evalRPN(["2","1","+","3","*"]) == 9
assert ob.evalRPN(["4","13","5","/","+"]) == 6
assert ob.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22