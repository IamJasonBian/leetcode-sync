class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        # Start from bottom-left corner
        row = len(matrix) - 1
        col = 0
        
        # While within bounds
        while row >= 0 and col < len(matrix[0]):
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                # If current is greater, go up
                row -= 1
            else:
                # If current is smaller, go right
                col += 1
                
        return False
