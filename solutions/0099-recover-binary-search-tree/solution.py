# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
       
        res = []     
        startnode = None
        prev = None
        lastnode = None
        
        def dfs(root):
            nonlocal res, startnode, prev, lastnode
            if not root:
                return 
            dfs(root.left)
            if prev and prev.val > root.val:
                if not startnode:
                    startnode = prev
                lastnode = root
            prev = root
            dfs(root.right)
        dfs(root)
        if startnode and lastnode:
            startnode.val, lastnode.val = lastnode.val, startnode.val
