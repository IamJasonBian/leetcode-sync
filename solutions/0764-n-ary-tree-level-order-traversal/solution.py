from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root]) # Initialize queue with root node
        result = [] # Initialize result list to store levels
        
        while queue:
            level = [] # Initialize list to store nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft() # Dequeue a node
                level.append(node.val) # Add node's value to the current level list
                
                # Enqueue all children of the current node
                for child in node.children:
                    queue.append(child)
            
            result.append(level) # Add the current level list to the result
        
        return result

