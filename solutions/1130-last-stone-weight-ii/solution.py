class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesum = sum(stones)
        half = stonesum // 2
        n = len(stones)
        dp = [[0 for j in range(half+1)]for _ in range(n)]

        for j in range(stones[0], half+1):
            dp[0][j] = stones[0]

        for i in range(1, n):
            for j in range(0, half+1):
                if j < stones[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]]+stones[i])
        return stonesum - dp[n-1][half] * 2
