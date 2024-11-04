class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        '''
        current_path = []

        def dfs(row, col, current_path):
            # Base case: reached bottom of matrix
            if row == rows:
                paths.append(current_path[:])
                return
                
            # Out of bounds check
            if col < 0 or col >= cols:
                return
                
            # Add current position to path
            current_path.append((matrix[row][col], row, col))
            
            # Recursive calls for all possible moves:
            # Down-left
            dfs(row + 1, col - 1, current_path)
            # Straight down
            dfs(row + 1, col, current_path)
            # Down-right
            dfs(row + 1, col + 1, current_path)
        
            current_path.pop()

        matrix = grid
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0

        for i in range(rows):
            for j in range(cols):
                if (matrix[i][j] == 1):  # only if the cell is a land
                    # we have found an island
                    totalIslands += 1
                    dfs(matrix, i, j)

        return totalIslands


        '''

        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1 
        
        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))
        
        # There was no path.
        return -1



        

      


