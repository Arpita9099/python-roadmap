class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def dfs(open, closed, s):

            if len(s) == n * 2:
                res.append(s)                

            if open < n:
                dfs(open + 1, closed, s + '(')

            if closed < open:
                dfs(open, closed + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
    
ob = Solution()
assert ob.generateParenthesis(2) == ['(())','()()']
assert ob.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
assert ob.generateParenthesis(1) == ["()"]
assert not ob.generateParenthesis(1) == ["())"]
