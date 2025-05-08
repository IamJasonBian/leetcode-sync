class Solution:
   def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
       n = len(security)
       result = []
       
       # Handle special cases
       if time == 0:
           return list(range(n))
           
       if n < 2 * time + 1:
           return []
       
       # Special optimization for time = 1 (length 3 subarrays)
       if time == 1:
           # For time = 1, we need to check 3-element subarrays
           # The pattern is: security[i-1] >= security[i] <= security[i+1]
           for i in range(1, n - 1):
               # Generate a subarray of length 3 centered at i
               subarray = [security[i-1], security[i], security[i+1]]
               
               # Check if current day forms a "valley" pattern
               if subarray[0] >= subarray[1] and subarray[1] <= subarray[2]:
                   result.append(i)
           return result
       
       # Original logic for all other time values
       # Count consecutive non-increasing days before each position
       non_increasing = [0] * n
       for i in range(1, n):
           if security[i] <= security[i - 1]:
               non_increasing[i] = non_increasing[i - 1] + 1
       
       # Count consecutive non-decreasing days after each position
       non_decreasing = [0] * n
       for i in range(n - 2, -1, -1):
           if security[i] <= security[i + 1]:
               non_decreasing[i] = non_decreasing[i + 1] + 1
       
       # Check each potential day
       for i in range(time, n - time):
           if non_increasing[i] >= time and non_decreasing[i] >= time:
               result.append(i)
       
       return result
