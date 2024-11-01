# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return -1
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # because left and right is guaranteed to have at least 2 here
            self.max_diameter = max(self.max_diameter, left_height + right_height + 2)
            return max(left_height, right_height) + 1
        
        dfs(root)
        return self.max_diameter
