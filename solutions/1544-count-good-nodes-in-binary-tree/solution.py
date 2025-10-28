# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        #val = 0
        # -- 0 is a bad initial bound 

        def dfs(node, val):

            if not node:
                return 0

            good = 1 if node.val >= val else 0
            new_max = max(val, node.val)  # ← ADD THIS
            good += dfs(node.left, new_max)   # ← Use new_max
            good += dfs(node.right, new_max)  # ← Use new_max

            return good

        return dfs(root, root.val)


