class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        startListIndex = 0
        endListIndex = len(matrix) - 1
        while (startListIndex <= endListIndex):
            midListIndex = (startListIndex +  endListIndex) // 2
            if matrix[midListIndex][0] > target:
                endListIndex = midListIndex - 1
            elif matrix[midListIndex][-1] < target:
                startListIndex = midListIndex + 1
            else:
                break
        
        if not(startListIndex <= endListIndex):
            return False
        
        startIndex = 0
        endIndex = len(matrix[0]) - 1
        subList = matrix[midListIndex]
        while (startIndex <= endIndex):
            midIndex = (startIndex +  endIndex) // 2
            if subList[midIndex] > target:
                endIndex = midIndex - 1
            elif subList[midIndex] < target:
                startIndex = midIndex + 1
            else:
                return True
        return False

ob = Solution()
assert ob.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3) == True
assert ob.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],12) == False
assert ob.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],11) == True