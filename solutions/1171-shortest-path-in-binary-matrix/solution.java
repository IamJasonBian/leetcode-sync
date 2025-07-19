class Solution {
    private static final int[][] DIRECTIONS = {
        {-1,-1}, {-1,0}, {-1,1},
        {0,-1},          {0,1},
        {1,-1},  {1,0}, {1,1}
    };

    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;
        
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][n];
        
        queue.offer(new int[]{0, 0, 1}); // [row, col, distance]
        visited[0][0] = true;
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int row = curr[0];
            int col = curr[1];
            int dist = curr[2];
            
            // Early termination: reached bottom-right
            if (row == n-1 && col == n-1) {
                return dist;
            }
            
            // Explore all 8 directions
            for (int[] dir : DIRECTIONS) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                
                if (newRow >= 0 && newRow < n && 
                    newCol >= 0 && newCol < n && 
                    !visited[newRow][newCol] && 
                    grid[newRow][newCol] == 0) {
                    
                    visited[newRow][newCol] = true;
                    queue.offer(new int[]{newRow, newCol, dist + 1});
                }
            }
        }
        
        return -1;
    }
}
