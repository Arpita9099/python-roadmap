class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        # ans = []

        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             ans.append(j-i)
        #             break
        #         if temperatures[i] >= temperatures[j] and j == len(temperatures)-1:
        #             ans.append(0)
        #     if i == len(temperatures)-1:
        #         ans.append(0)
        # return(ans)

        res = [0] * len(temperatures) 
        stack = [] # pair: [temp,index]

        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp,stackIndex = stack.pop()
                res[stackIndex] = (index - stackIndex)
            stack.append([temp,index])

        return res
        

ob = Solution()
assert ob.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert ob.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert ob.dailyTemperatures([30,60,90]) == [1,1,0]
