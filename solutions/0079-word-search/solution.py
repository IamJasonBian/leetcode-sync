class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True
        return False

    def dfs(self, board: List[List[str]], i: int, j: int, count: int, word: str) -> bool:
        if count == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
            return False
        
        # template based backtracking: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/

        temp = board[i][j]
        board[i][j] = '*'
        found = self.dfs(board, i + 1, j, count + 1, word) or \
                self.dfs(board, i - 1, j, count + 1, word) or \
                self.dfs(board, i, j + 1, count + 1, word) or \
                self.dfs(board, i, j - 1, count + 1, word)
        board[i][j] = temp
        return found
