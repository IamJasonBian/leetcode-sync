class PalindromeTable:
    """Class to handle palindrome computations and storage"""
    def __init__(self, string: str):
        self.string = string
        self.length = len(string)
        self.table = [[False] * self.length for _ in range(self.length)]
        self._precompute_palindromes()
    
    def _precompute_palindromes(self) -> None:
        """Precomputes all palindrome substrings"""
        # Single characters are palindromes
        for i in range(self.length):
            self.table[i][i] = True
            
        # Check palindromes of length 2 and more
        for length in range(2, self.length + 1):
            for start in range(self.length - length + 1):
                end = start + length - 1
                if length == 2:
                    self.table[start][end] = (self.string[start] == self.string[end])
                else:
                    self.table[start][end] = (self.string[start] == self.string[end] and 
                                            self.table[start + 1][end - 1])
    
    def is_palindrome(self, start: int, end: int) -> bool:
        """Check if substring from start to end is palindrome"""
        return self.table[start][end]


class PalindromeCutSolver:
    """Class to solve minimum palindrome cut problem"""
    def __init__(self, string: str):
        self.string = string
        self.length = len(string)
        self.dp = [-1] * self.length
        self.palindrome_table = PalindromeTable(string)
    
    def _find_min_cut(self, start: int) -> int:
        """Recursive helper to find minimum cuts needed"""
        # Base cases
        if start >= self.length:
            return 0
            
        # Return memoized result if available
        if self.dp[start] != -1:
            return self.dp[start]
            
        # If remaining string is palindrome, no cuts needed
        if self.palindrome_table.is_palindrome(start, self.length - 1):
            self.dp[start] = 0
            return 0
            
        # Try all possible cuts and take minimum
        min_cuts = self.length
        for i in range(start, self.length):
            if self.palindrome_table.is_palindrome(start, i):
                min_cuts = min(min_cuts, 1 + self._find_min_cut(i + 1))
                
        self.dp[start] = min_cuts
        return min_cuts
    
    def solve(self) -> int:
        """Public method to find minimum cuts needed"""
        if not self.string:
            return 0
        return self._find_min_cut(0)


class Solution:
    """LeetCode solution class"""
    def minCut(self, s: str) -> int:
        solver = PalindromeCutSolver(s)
        return solver.solve()



