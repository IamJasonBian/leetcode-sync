class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left: int, in_right: int, post_left: int, post_right: int) -> TreeNode:
            if in_left > in_right:
                return None

            root_val = postorder[post_right]
            root = TreeNode(root_val)
            idx = idx_map[root_val]

            # which element of in/post order we are currently sitting on
            left_size = idx - in_left
            root.left = helper(in_left, idx - 1, post_left, post_left + left_size - 1)
            root.right = helper(idx + 1, in_right, post_left + left_size, post_right - 1)
            
            return root
        
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
