class Solution:
    def maxProfit(self, prices: list[int]) -> int: 
        l = 0 # Buying Pointer
        r = 1 # Selling Pointer
        maxprofit = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                if profit > maxprofit:
                    maxprofit = profit
            else:
                l = r
            r = r + 1
        return maxprofit

ob = Solution()
assert ob.maxProfit([7,1,5,3,6,4]) == 5
assert ob.maxProfit([7,6,4,3,1]) == 0
assert not ob.maxProfit([7,6,4,3,1]) == 1