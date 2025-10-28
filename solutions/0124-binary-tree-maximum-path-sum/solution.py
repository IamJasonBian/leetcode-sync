# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float('-inf')

        def maxG(node):
            if not node:
                return 0
            # parent child linking
            left_g = max(0, maxG(node.left))
            right_g = max(0, maxG(node.right))
            path = node.val + left_g + right_g
            self.max_sum = max(self.max_sum, path)
            return node.val + max(left_g, right_g)

        maxG(root)
        return self.max_sum

