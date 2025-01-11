class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Find the shortest path from top-left to bottom-right corner in a binary matrix.
        A path can only move through cells containing 0, and can move in 8 directions.
        
        Args:
            grid (List[List[int]]): Binary matrix where 0 represents passable cells 
                                   and 1 represents blocked cells
        
        Returns:
            int: Length of shortest path from (0,0) to (n-1,n-1), or -1 if no path exists
        
        Time complexity: O(n²) where n is the size of the grid
        Space complexity: O(n²) for the queue in worst case
        """
        # Edge cases: empty grid or blocked start/end points
        if not grid or not grid[0]:
            return -1
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        n = len(grid)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        # Use queue for BFS instead of stack for shortest path
        from collections import deque
        queue = deque([(0, 0, 1)])  # (x, y, path_length)
        grid[0][0] = 1  # Mark as visited
        
        while queue:
            x, y, path_length = queue.popleft()
            
            if x == n - 1 and y == n - 1:
                return path_length
            
            # Explore all 8-connected neighbors
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                # Check bounds and if cell is unvisited (0)
                if (0 <= new_x < n and 
                    0 <= new_y < n and 
                    grid[new_x][new_y] == 0):
                    
                    grid[new_x][new_y] = 1  # Mark as visited
                    queue.append((new_x, new_y, path_length + 1))
        
        return -1  # No valid path found
