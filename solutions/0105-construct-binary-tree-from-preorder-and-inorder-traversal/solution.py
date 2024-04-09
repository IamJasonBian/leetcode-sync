from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        # Find the root in the inorder traversal
        rootIndexInorder = inorder.index(preorder[0])
        
        # The elements before the root in the inorder traversal are in the left subtree
        # The elements after the root in the inorder traversal are in the right subtree
        leftSubtreeInorder = inorder[:rootIndexInorder]
        rightSubtreeInorder = inorder[rootIndexInorder+1:]
        
        # The elements after the root in the preorder traversal are in the right subtree
        # The elements before the root in the preorder traversal are in the left subtree
        leftSubtreePreorder = preorder[1:len(leftSubtreeInorder)+1]
        rightSubtreePreorder = preorder[len(leftSubtreeInorder)+1:]
        
        root.left = self.buildTree(leftSubtreePreorder, leftSubtreeInorder)
        root.right = self.buildTree(rightSubtreePreorder, rightSubtreeInorder)
        
        return root


