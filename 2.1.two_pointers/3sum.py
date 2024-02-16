class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums_sorted = sorted(nums)
        print(f'nums_sorted:{nums_sorted}')
        for i in range(len(nums_sorted)-2):
            j = i+1
            k = len(nums_sorted) - 1
            while (j < k):
                if nums_sorted[i] + nums_sorted[j] + nums_sorted[k] == 0:
                    l.append((nums_sorted[i],nums_sorted[j],nums_sorted[k]))
                    j += 1
                elif nums_sorted[i] + nums_sorted[j] + nums_sorted[k] > 0:
                    k -= 1
                else:
                    j += 1
        return(set(l))
    
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans=set()
#         nums.sort()
#         n=len(nums)
#         for i in range(n-2):
#             for j in range(i+1,n-1):
#                 for k in range(j+1,n):
#                     temp=nums[i]+nums[j]+nums[k]
#                     if temp==0:
#                         ans.add((nums[i],nums[j],nums[k]))
#         return ans