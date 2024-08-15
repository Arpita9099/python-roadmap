## Simple approch
# output = []

# def get_all_substrings(input_string) -> list:
#     if len(input_string) == 0:
#         return []
#     elif len(input_string) == 1:
#         return[input_string]
#     else:
#         for i in range(len(input_string)):
#             for j in range(i+1,len(input_string)+1):
#                 sub = input_string[i:j]
#                 print(sub)
#                 if len(sub) == len(set(sub)):
#                     output.append(input_string[i:j])
#         return output 
    
# def lenCount(s):
#     return len(s)

# my_string = "hello"
# substrings = get_all_substrings(my_string)
# print(substrings)
# lenList = map(lenCount,output)
# print(max(list(lenList)))

## Useing set
# class Solution:
#     def lengthOfLongestSubstring(self, s:str) -> int:
#         charSet = set()
#         leftPointer = 0
#         result = 0

#         for rightPointer in range(len(s)):
#             while s[rightPointer] in charSet:
#                 charSet.remove(s[leftPointer])
#                 leftPointer += 1
#             charSet.add(s[rightPointer])
#             result = max(result, rightPointer - leftPointer + 1)
#         return result

# ob = Solution()
# assert ob.lengthOfLongestSubstring('bcabcbb') == 3


## Using List
# class Solution:
#     def lengthOfLongestSubstring(self, s:str) -> int:
#         substring = []
#         leftPointer = 0
#         result = 0

#         for rightPointer in range(len(s)):
#             if s[rightPointer] in substring:
#                 t = s[rightPointer]
#                 leftPointer = substring.index(t) 
#                 substring = substring[leftPointer+1:]
#             substring.append(s[rightPointer])     
#             result = max(result, len(substring))
#         return result

# ob = Solution()
# assert ob.lengthOfLongestSubstring('bcabcbb') == 3


## Using Dicstionary
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        chars = {}
        leftPointer = 0
        result = 0

        for rightPointer in range(len(s)):
            if s[rightPointer] in chars:
                leftPointer = chars[s[rightPointer]] + 1
            chars[s[rightPointer]] = rightPointer
            result = max(result, rightPointer - leftPointer + 1)
        return result

ob = Solution()
assert ob.lengthOfLongestSubstring('bcabcbb') == 3
