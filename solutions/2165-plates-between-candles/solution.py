from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left_candle = [-1] * n
        right_candle = [n] * n
        prefix = [0] * (n + 1)
        
        last = -1
        for i in range(n):
            if s[i] == '|':
                last = i
            left_candle[i] = last
        
        last = n
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                last = i
            right_candle[i] = last
        
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if s[i] == '*' else 0)
        
        result = []
        for l, r in queries:
            left = right_candle[l]
            right = left_candle[r]
            
            if left == n or right == -1 or left >= right:
                result.append(0)
            else:
                result.append(prefix[right+1] - prefix[left])
        
        return result
