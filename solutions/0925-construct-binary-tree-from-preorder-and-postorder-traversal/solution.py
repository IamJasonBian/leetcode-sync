class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        num_of_nodes = len(preorder)
        index_in_post_order = [0] * (num_of_nodes + 1)
        for index in range(num_of_nodes):
            index_in_post_order[postorder[index]] = index

        return self._construct_tree(
            0, num_of_nodes - 1, 0, preorder, index_in_post_order
        )
    def _construct_tree(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        index_in_post_order: List[int],
    ) -> Optional[TreeNode]:

        if pre_start > pre_end:
            return None


        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        left_root = preorder[pre_start + 1]
        num_of_nodes_in_left = index_in_post_order[left_root] - post_start + 1

        root = TreeNode(preorder[pre_start])
        root.left = self._construct_tree(
            pre_start + 1,
            pre_start + num_of_nodes_in_left,
            post_start,
            preorder,
            index_in_post_order,
        )
        root.right = self._construct_tree(
            pre_start + num_of_nodes_in_left + 1,
            pre_end,
            post_start + num_of_nodes_in_left,
            preorder,
            index_in_post_order,
        )

        return root
