class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node, val):
            if not node:
                return 0

            op = 0
            if (node.val >= val):
                op = 1
            
            val = max(val, node.val)
            return op + dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, root.val)
