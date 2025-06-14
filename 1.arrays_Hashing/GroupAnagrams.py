# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         d1 = {}
#         d2 = {}
#         for ch in s:
#             if ch in d1.keys():
#                 d1[ch] = d1[ch] + 1
#             else:
#                 d1[ch] = 1
#         for ch in t:
#             if ch in d2.keys():
#                 d2[ch] = d2[ch] + 1
#             else:
#                 d2[ch] = 1
#         if d1 == d2:
#             return True
#         return False
    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
           return True
        return False 


ob = Solution()
assert ob.isAnagram("racecar", "carrace") == True
assert ob.isAnagram("jar", "jam") == False
assert ob.isAnagram("xx", "x") == False