from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(26):
                prefix[i+1][j] = prefix[i][j]
            prefix[i+1][ord(s[i]) - ord('a')] += 1
        
        result = []
        for l, r, k in queries:
            odd = 0
            for i in range(26):
                if (prefix[r+1][i] - prefix[l][i]) % 2 == 1:
                    odd += 1
            result.append(odd // 2 <= k)
        
        return result
