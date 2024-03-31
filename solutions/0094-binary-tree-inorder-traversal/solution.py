from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> int:
        # Initialize a list to store the in-order traversal
        inorder_list = []
        
        # Helper function to perform in-order traversal
        def inorder(node):
            if node:
                inorder(node.left)
                inorder_list.append(node.val)
                inorder(node.right)
        
        # Start in-order traversal
        inorder(root)
        
        # Return the kth smallest element
        return inorder_list
