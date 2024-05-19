from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        # Helper function to perform DFS
        def dfs(node, curr_path, curr_sum):
            if not node:
                return
            
            # Add the current node's value to the current sum
            curr_sum += node.val
            curr_path.append(node.val)
            
            # Check if the current node is a leaf and the current sum matches the target sum
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(list(curr_path))
            else:
                # Recurse on the left and right children
                dfs(node.left, curr_path, curr_sum)
                dfs(node.right, curr_path, curr_sum)
            
            # Backtrack by removing the last node from the current path
            curr_path.pop()
        
        result = []
        dfs(root, [], 0)
        return result

