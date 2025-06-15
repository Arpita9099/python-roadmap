class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for num in nums:
            if num in d.keys():
                d[num] = d[num] + 1
            else:
                d[num] = 1
        l = []
        while len(l) < k:
            tk = -1
            tv = -1
            for n, v in d.items():
                if v > tv and n not in l:
                    tk = n
                    tv = v
            l.append(tk)
        return l                  


ob = Solution()
assert ob.topKFrequent([1,2,2,3,3,3], 2) == [3,2]