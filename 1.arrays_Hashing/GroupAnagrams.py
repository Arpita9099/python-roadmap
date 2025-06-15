class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for l in strs:
            if tuple(sorted(l)) in d.keys():
                d[tuple(sorted(l))].append(l)
            else:
                d[tuple(sorted(l))] = [l]
        return (list(d.values()))



ob = Solution()
assert ob.groupAnagrams(["act","pots","tops","cat","stop","hat"]) == [['act', 'cat'],['pots', 'tops', 'stop'],['hat']]