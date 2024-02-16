# import string

# class Solution:
#     def isPalindrome(self, s: str) -> bool:

#         l = string.ascii_lowercase + string.digits

#         # Convert string into lower letter
#         s = s.lower()

#         # remov all non-alphanumeric characters
#         s = [item for item in s if item in l]

#         # check reverse sequence
#         t = len(s)//2
#         for i in range(t):
#             if s[i] != s[-i-1]:
#                 return False
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True