import numpy as np
class Solution:
    def contains_duplicates(self, X):
        X = X[X != '.']
        return len(np.unique(X)) != len(X)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = np.array(board)
        arrt = arr.T
        
        b = np.transpose(np.transpose(np.transpose(arr.reshape((3, 3, 9)), (1, 0, 2)).reshape((3, -1))).reshape((9, 3, 3)), (0, 2, 1))
                
        for i in b:
            if self.contains_duplicates(i.reshape(9,1)):
                return False
            
        for row in arr:
            if self.contains_duplicates(row):
                return False
            
        for col in arrt:
            if self.contains_duplicates(col):
                return False
        return True
        
