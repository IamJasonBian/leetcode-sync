class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = grid[0]
        
        for r in range(1, N):
            next_dp = [float("inf")] * N
            for curr_c in range(N):
                for prev_c in range(N):
                    if prev_c != curr_c:
                        next_dp[curr_c] = min(
                            next_dp[curr_c],
                            grid[r][curr_c] + dp[prev_c]    
                        )
                        
            dp = next_dp
        return min(dp)
    
    
