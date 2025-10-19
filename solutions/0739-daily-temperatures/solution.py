class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize result array with zeros
        stack = []  # Stack stores indices of temperatures
        
        for i in range(n):
            # While stack is not empty and current temp is warmer than temp at stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index  # Days to wait
            
            stack.append(i)  # Push current index onto stack
        
        # Remaining indices in stack have no warmer day (already initialized to 0)
        return answer



