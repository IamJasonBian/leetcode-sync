class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        # Check if the lengths of s1, s2, and s3 are consistent
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Initialize the DP table, True is the base/ if s3 is empty, s1 and s2 can interleave to form s3
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        
        # Fill the DP table
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):

                # Note that Inputs can be empty strings
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])

                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        # The last cell will contain the final answer (True/False)
        return dp[-1][-1]
