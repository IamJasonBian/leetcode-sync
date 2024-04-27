class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length;
        int[][] dp = new int[n+1][n];
        
        // Initialize the base case for the first row
        for (int j = 0; j < n; j++) {
            dp[0][j] = grid[0][j];
        }
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int minSum = Integer.MAX_VALUE;
                for (int k = 0; k < n; k++) {
                    if (k != j) {
                        minSum = Math.min(minSum, dp[i-1][k]);
                    }
                }
                dp[i][j] = minSum + grid[i][j];
            }
        }
        
        // Find the minimum sum in the last row
        int minSum = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            minSum = Math.min(minSum, dp[n-1][j]);
        }
        
        return minSum;
    }
}

