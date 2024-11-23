class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        cur, pre, preRight = root, None, None
        while cur:
            temp1, temp2 = cur.left, cur.right
            cur.left, cur.right = preRight, pre
            cur, pre, preRight = temp1, cur, temp2
        return pre
