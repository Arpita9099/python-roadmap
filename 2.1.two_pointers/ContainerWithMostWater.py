class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height)-1
        while(i <= j):
            if height[i] < height[j]:
                t = height[i] * (j-i)
                if t > max_area:
                    max_area = t
                i +=1
            else:
                t = height[j] * (j-i)
                if t > max_area:
                    max_area = t
                j -=1
        return (max_area)