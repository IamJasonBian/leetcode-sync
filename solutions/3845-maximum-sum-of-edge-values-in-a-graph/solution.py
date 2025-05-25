class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:

        curve1 = (((2*n + 3)*n - 11)*n + 6) // 6
        curve2 = 2*(n == len(edges))

        return curve1 + curve2
