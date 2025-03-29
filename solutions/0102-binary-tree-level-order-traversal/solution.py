class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Performs level order traversal of a binary tree.
        
        Args:
            root: The root of the binary tree
            
        Returns:
            A list of lists where each inner list contains the values 
            of nodes at that level from left to right
        """
        # Handle empty tree case
        if not root:
            return []
        
        result = []
        queue = [root]  # Initialize queue with root node
        
        while queue:
            # Get the number of nodes at current level
            level_size = len(queue)
            level_values = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.pop(0)  # Dequeue node
                level_values.append(node.val)
                
                # Enqueue children for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add current level's values to result
            result.append(level_values)
        
        return result

