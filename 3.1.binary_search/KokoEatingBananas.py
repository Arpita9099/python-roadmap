import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)        
        result = r
        while (l <= r):
            k = (l + r) // 2
            hours = 0
            for i in range(len(piles)):
                hours = hours + math.ceil(piles[i] / k)
            if hours <= h:
                result = min(result,k)
                r = k - 1
            else:
                l = k + 1
        return result     

ob = Solution()
assert ob.minEatingSpeed([3,6,7,11],8) == 4
assert ob.minEatingSpeed([30,11,23,4,20],5) == 30
assert ob.minEatingSpeed([30,11,23,4,20],6) == 23