from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if node is None, return None
        if not root:
            return None
        
        # DFS: recursively process left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        print(root.left)
        if root.val == 0 and not root.left and not root.right: # this would cascade back up 
            return None

        return root

