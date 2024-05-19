class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # This traverses through and adds up all the sums into target sum using a truth operator
        
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
