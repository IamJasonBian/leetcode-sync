from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # Use defaultdict to store column-wise values
        columns = defaultdict(list)
        
        # Queue to store node and its column position
        queue = deque([(root, 0)])
        
        # Track min and max columns to avoid sorting later
        min_col = max_col = 0
        
        # BFS traversal
        while queue:
            node, col = queue.popleft()
            
            # Add current node's value to its column
            columns[col].append(node.val)
            
            # Update min and max column values
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            # Add left child with column position - 1
            if node.left:
                queue.append((node.left, col - 1))
            
            # Add right child with column position + 1
            if node.right:
                queue.append((node.right, col + 1))
        
        # Construct result using tracked min and max columns
        return [columns[col] for col in range(min_col, max_col + 1)]
