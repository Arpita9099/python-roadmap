class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        c = 1
        longestsequence = 1
        s = sorted(nums)
        print(s)
        # get one item through for loop
        for i in range(1,len(s)):
            if s[i] - s[i-1] == 1:
                c = c+1
            elif s[i] - s[i-1] != 0:
                if c > longestsequence:
                    longestsequence = c 
                c = 1

        if c > longestsequence and len(s) != 0:
            longestsequence = c          

        return(longestsequence)