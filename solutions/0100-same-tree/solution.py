from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both trees are empty
        if p is None and q is None:
            return True
        # One of the trees is empty, but not the other
        if p is None or q is None:
            return False
        # Both trees are not empty, compare their values and recursively check their subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

