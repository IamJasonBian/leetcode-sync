class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        n = len(nums)
        m = len(queries)
        dp = [[0 for j in range(n+1)] for i in range(n+1)]
        for l in range(n,-1,-1):
            for i in range(n-l+1):
                j = i+l
                if i > 0:
                    prev = dp[i-1][j]
                    if prev == m: dp[i][j] = prev
                    elif queries[prev]<=nums[i-1]:
                        dp[i][j] = max(dp[i][j],prev+1)
                    else:
                        dp[i][j] = max(prev,dp[i][j])
                if j<n:
                    post = dp[i][j+1]
                    if post == m:dp[i][j] = post
                    elif queries[post]<=nums[j]:
                        dp[i][j] = max(dp[i][j],post+1)
                    else:
                        dp[i][j] = max(post,dp[i][j])
        return max(dp[i][i] for i in range(n+1))
        
