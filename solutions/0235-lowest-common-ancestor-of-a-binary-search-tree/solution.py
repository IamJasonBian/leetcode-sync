# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

    
        def findLCA(node: 'TreeNode', p: int, q: int) -> 'TreeNode':
            if not node:
                return None
            
            if p.val > node.val and q.val > node.val:
                return findLCA(node.right, p, q)
    
            if p.val < node.val and q.val < node.val:
                return findLCA(node.left, p, q)

            return node

        return findLCA(root, p, q)
