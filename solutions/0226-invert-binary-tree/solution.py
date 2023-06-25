class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root is None: return 
            temp1 = root.left
            temp2 = root.right
            root.left = temp2
            root.right = temp1
            invert(root.left)
            invert(root.right)
        invert(root)
        return root
