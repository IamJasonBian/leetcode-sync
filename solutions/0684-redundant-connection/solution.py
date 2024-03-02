from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1)) # Initialize parent array
        
        def find(x):
            # Find the root of x
            if parent[x] != x:
                parent[x] = find(parent[x]) # Path compression
            return parent[x]
        
        def union(x, y):
            # Union two nodes
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                return True
            return False
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        
        return edges[-1] # If no cycle is found, the last edge is redundant

