from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        """
        
            Go Inwards

        """

        m, n = len(board), len(board[0])
        # "Corrupted" cells from the boundary
        boundary_bfs = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if     board[i][j] == 'O' and (i in (0, m - 1) or j in (0, n - 1)):
                    if (i, j) not in visited:  # Extra safety check
                        boundary_bfs.append((i, j))
                        visited.add((i, j))

        print(boundary_bfs)
        while boundary_bfs:
            r, c = boundary_bfs.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Traverse and find all Os
                if (0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O' and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    boundary_bfs.append((nr, nc))

        print(boundary_bfs)
        print(visited)
        print(board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        
        print(f"Final board: {board}")









        
       
