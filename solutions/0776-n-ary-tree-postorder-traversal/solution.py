class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Initialize a list to store the post-order traversal
        postorder_list = []
        
        # Helper function to perform post-order traversal
        def postorder_traversal(node):
            if node:
                # Recursively visit all children
                for child in node.children:
                    postorder_traversal(child)
                # After visiting all children, append the current node's value
                postorder_list.append(node.val)
        
        # Start post-order traversal
        postorder_traversal(root)
        
        # Return the post-order traversal list
        return postorder_list

