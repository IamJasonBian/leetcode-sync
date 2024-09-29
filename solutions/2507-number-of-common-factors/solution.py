class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = 0
        for i in range(1, min([a, b]) + 1) :
            if not a % i and not b % i :
                c += 1
        return c
