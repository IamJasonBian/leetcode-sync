# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            # Initialize a list to store the in-order traversal
            postorder_list = []
            
            # Helper function to perform in-order traversal
            def postorder(node):
                if node:
                    postorder(node.left)
                    postorder(node.right)
                    postorder_list.append(node.val)
            
            # Start in-order traversal
            postorder(root)
            
            # Return the kth smallest element
            return postorder_list
