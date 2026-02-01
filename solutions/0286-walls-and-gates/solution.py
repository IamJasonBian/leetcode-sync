class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        

        """
        
            Do not return anything, modify rooms in-place instead

            m x n grid - rooms filled with

                -1: Wall or an obstacle
                0: A gate
                INF: 

            BFS from gate to every room etc  

        """

        INF = 2147483647
        print(rooms)
        m, n = len(rooms), len(rooms[0])
        doors_bfs = deque()
        
        visited = set()

        # append gates as 0
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    doors_bfs.append((i,j))

        # door bfs (if another door got to it then skippo)
        while doors_bfs:
            r, c = doors_bfs.popleft()
            current_dist = rooms[r][c]

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    #make the pass to close the loop
                    rooms[nr][nc] = current_dist + 1
                    doors_bfs.append((nr, nc))

        print(doors_bfs) 
        print(visited)

        

