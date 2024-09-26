class Solution {
    public boolean searchMatrix(int[][] matrix, int t) {
        int m = matrix.length;
        int n = matrix[0].length;
        int left = 0, right = m * n - 1;
        while(left <= right)
        {
            int mid = (left + right) / 2;
            int rowIdx = mid / n;
            int colIdx = mid % n;
            if(matrix[rowIdx][colIdx] == t) return true;
            else if(t > matrix[rowIdx][colIdx]) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
}
