class Solution {
    private List<List<String>> result;
    private boolean[][] dp;
    private char[] chars;
    
    public List<List<String>> partition(String s) {
        result = new ArrayList<>();
        chars = s.toCharArray();
        int n = chars.length;
        dp = new boolean[n][n];
        
        // Precompute palindromes + backtracking
        computePalindromes(n);
        backtrack(0, new ArrayList<>());
        
        return result;
    }
    
    private void computePalindromes(int n) {
        // Single characters are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        
        // Check palindromes for substrings
        for (int len = 2; len <= n; len++) {
            for (int start = 0; start <= n - len; start++) {
                int end = start + len - 1;
                if (len == 2) {
                    dp[start][end] = chars[start] == chars[end];
                } else {
                    dp[start][end] = chars[start] == chars[end] && dp[start + 1][end - 1];
                }
            }
        }
    }
    
    private void backtrack(int start, List<String> current) {
        if (start >= chars.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int end = start; end < chars.length; end++) {
            sb.append(chars[end]);
            if (dp[start][end]) {
                current.add(sb.toString());
                backtrack(end + 1, current);
                current.remove(current.size() - 1);
            }
        }
    }
}
