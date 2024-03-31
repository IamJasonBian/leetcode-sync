class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Initialize a list to store the post-order traversal
        preorder_list = []
        
        # Helper function to perform post-order traversal
        def preorder_traversal(node):
            if node:

                
                preorder_list.append(node.val)
                for child in node.children:
                    preorder_traversal(child)
               
        
        # Start post-order traversal
        preorder_traversal(root)
        
        # Return the post-order traversal list
        return preorder_list

