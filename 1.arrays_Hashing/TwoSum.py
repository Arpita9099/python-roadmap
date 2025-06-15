class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            j = 1
            while len(nums) > j:
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
                else:
                    j = j+1


ob = Solution()
assert ob.twoSum([3,4,5,6],7) == [0,1]
assert ob.twoSum([5,5],10) == [0,1]
assert ob.twoSum([2,5,5,11], 10) == [1,2]