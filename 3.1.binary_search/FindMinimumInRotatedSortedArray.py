class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        result = nums[0]
        while(l <= r):
            if nums[l] < nums[r]:
                result = min(result,nums[l])
                break
            m = (l + r) // 2
            result = min(result,nums[m])
            if (nums[m] >= nums[l]):
                l = m + 1
            else:
                r = m - 1
        return result

ob = Solution()
assert ob.findMin([3,4,5,1,2]) == 1
assert ob.findMin([4,5,6,7,0,1,2]) == 0
assert ob.findMin([11,13,15,17]) == 11