class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        t = list(zip(position,speed))
        l = []
        stack = []
        for i in t:
            l.append(list(i))
        s_l = sorted(l)
        s_l_r = s_l[::-1] # reverse 
        for p,s in s_l_r:
            stack.append((target - p)/s) # time to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return(len(stack))

ob = Solution()
assert ob.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]) == 3
assert ob.carFleet(10,[3],[3]) == 1
assert ob.carFleet(100,[0,2,4],[4,2,1]) == 1