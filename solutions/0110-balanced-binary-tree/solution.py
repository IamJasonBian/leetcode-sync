from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Check if the current subtree is balanced
            if abs(left_height - right_height) > 1:
                
                # Not balanced!!! 
                return float('-inf')
            else:
                return 1 + max(left_height, right_height)
        
        # Calculate the height of the entire tree
        tree_height = dfs(root)
        
        # Return True if the tree is balanced (i.e., its height is not negative)
        return tree_height != float('-inf')
