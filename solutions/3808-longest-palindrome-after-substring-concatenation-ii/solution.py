class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def check(a):
            ans = [1]*len(a)+[0]
            # longest palindrome beginning at index i in string a
            for k in range(len(a)):
                i, j = k, k
                while i>=0 and j<len(a) and a[i]==a[j]:
                    ans[i] = max(ans[i], j-i+1)
                    i, j = i-1, j+1
                i, j = k, k+1
                while i>=0 and j<len(a) and a[i]==a[j]:
                    ans[i] = max(ans[i], j-i+1)
                    i, j = i-1, j+1
            return ans

        res1, res2 = check(s), check(t[::-1])

        def lcs(a, b):
            dp, ans = [[0]*(len(b)+1) for _ in range(len(a)+1)], 1
            for i in range(len(a)):
                for j in range(len(b)):
                    if a[i]==b[j]:
                        dp[i+1][j+1] = dp[i][j]+1
                    cur = dp[i+1][j+1]*2+max(res1[i+1], res2[j+1])
                    ans = max(cur, ans)
            return ans
        return max(lcs(s, t[::-1]), max(res1), max(res2))
