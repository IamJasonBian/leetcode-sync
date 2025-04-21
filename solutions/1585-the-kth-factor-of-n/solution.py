class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        large_factors = []

        "factor pair straddling on both sides of the curve"
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
                if i != n // i:
                    large_factors.append(n // i)
        if k > len(large_factors):
            return -1

        return large_factors[len(large_factors) - k]
