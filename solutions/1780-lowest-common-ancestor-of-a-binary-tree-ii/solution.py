class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.res = None
        
        def helper(node):
            if not node:
                return 0
            
            cur = node == p or node == q
            left = helper(node.left)
            right = helper(node.right)
            
            if cur+left+right == 2 and not self.res:
                self.res = node
            return cur+left+right
                
        helper(root)
        return self.res
            
