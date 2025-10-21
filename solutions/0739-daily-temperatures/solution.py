class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        result = [0] * n
        stack = [] #store indices

        for i , temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
               
                # stack compounding etc 
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
                # print(stack)
            stack.append(i)
        return result
        
