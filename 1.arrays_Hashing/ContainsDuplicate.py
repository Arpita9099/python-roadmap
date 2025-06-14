# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#      #   print(f'set:{len(set(nums))} list: {len(nums)}')
#         if len(nums) == len(set(nums)):
#             return False
#         return True

# ob = Solution()
# assert ob.hasDuplicate([1,3,2,2]) == True
# assert ob.hasDuplicate([1,3,5,2]) == False
# assert ob.hasDuplicate([2,2]) == True

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        l = []
        for num in nums:
            if num in l:
                return True
            else:
                l.append(num)
        return False
ob = Solution()
assert ob.hasDuplicate([1,3,2,2]) == True
assert ob.hasDuplicate([1,3,5,2]) == False
assert ob.hasDuplicate([2,2]) == True