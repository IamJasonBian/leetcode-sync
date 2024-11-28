# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        """

        Find the lowest common ancestor of two nodes in a binary tree.
        Uses parent pointers and a set to track ancestors.
        
        Time complexity: O(h) where h is the height of the tree
        Space complexity: O(h) to store ancestors
        
        Args:
            p: First node
            q: Second node
            
        Returns:
            The lowest common ancestor node
            
        """

        ancestors = set()
        current = p
        while current:
            ancestors.add(current)
            current = current.parent
            
        current = q
        while current:
            if current in ancestors:
                return current
            current = current.parent
            
        return None
