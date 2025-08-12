from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        powers = []
        for i in range(n.bit_length()):
            if n & (1 << i):
                powers.append(1 << i)
        
        answers = []
        for left, right in queries:
            prod = 1
            for i in range(left, right + 1):
                prod = (prod * powers[i]) % MOD
            answers.append(prod)
        return answers
