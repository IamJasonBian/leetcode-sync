# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize a list to store the in-order traversal
        preorder_list = []
        
        # Helper function to perform in-order traversal
        def order(node):
            if node:

                preorder_list.append(node.val)
                order(node.left)
                order(node.right)
                
        # Start in-order traversal
        order(root)
        
        # Return the kth smallest element
        return preorder_list

