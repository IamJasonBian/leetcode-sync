# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_values = [node.val for node in nodes]
        ancestors = []
        
        def find_matching_nodes(root: TreeNode) -> int:
            if not root:
                return 0
                
            match_count = 0
            match_count += find_matching_nodes(root.left)
            match_count += find_matching_nodes(root.right)

            if root.val in node_values:
                match_count += 1

            if match_count == len(node_values):
                ancestors.append(root)
                
            return match_count
            
        find_matching_nodes(root)

        return ancestors[0] if ancestors else None


