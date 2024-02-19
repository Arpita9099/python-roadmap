class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                # if len(stack) != 0 and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False

ob = Solution()

assert ob.isValid('()')
assert ob.isValid('{}')
assert ob.isValid('[]')
assert ob.isValid('([[{()}]])')
assert  not ob.isValid('{(})')
assert  not ob.isValid('{[}]()')
assert  not ob.isValid('[{[}]()]')


