class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else :
                r=m-1
        return -1

# class Solution:
#     def search(self, nums: list[int], target: int):
#         startIndex = 0
#         endIndex = len(nums) - 1
#         return self.findEnlement(nums,startIndex,endIndex,target)

#     def findEnlement(self,num,startIndex,endIndex,target) -> int:
#         if startIndex > endIndex:
#             return -1
        
#         midIndex = (startIndex + endIndex) // 2
        
#         if num[midIndex] < target:
#             startIndex = midIndex + 1
#             return self.findEnlement(num,startIndex,endIndex,target)
#         elif num[midIndex] == target:
#             return midIndex
#         elif num[midIndex] > target:
#             endIndex = midIndex - 1
#             return self.findEnlement(num,startIndex,endIndex,target)

ob = Solution()
assert ob.search([1,3,5,7,9],3) == 1
assert ob.search([1,3,5,7,9,10],10) == 5
assert ob.search([1,3,5,7,8,9],7) == 3
assert ob.search([1,3,5,7,9],4) == -1
assert not ob.search([1,3,5,7,9],4) == 4