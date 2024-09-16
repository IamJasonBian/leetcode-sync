# Time complexity : O(m×n+L) where L is the number of operations, 
# m is the number of rows and nnn is the number of columns. 
# it takes O(m×n) to initialize UnionFind, and O(L) to process positions. 
# Space complexity: O(m×n)  as required by UnionFind data structure:
class UnionFind:
    # 1) Create Union-Find containers: 
    def __init__(self,N):
        self.rank = [0]*N
        self.parents = [i for i in range(N)]
        
    # 2) Search for parent node
    def find(self, node):
        while node != self.parents[node]:
            node = self.parents[node]
            self.parents[node] = self.parents[self.parents[node]]

        return node

    # 3) Connects 2 nodes by making p1 the parent of p2: 
    def union(self, parent, child):
        p1 = self.find(parent)
        p2 = self.find(child)
        
        # Check we're not in the same node:
        if p1 == p2: 
            return False
        
        # Rank operation (Get height):
        # Attach smaller depth tree under the root of the deeper tree:
        p1_rank = self.rank[parent]
        p2_rank = self.rank[child]
        
        if p1_rank == p2_rank:
            self.parents[p1] = p2
            self.rank[child] += 1
            
        elif p1_rank < p2_rank:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            
        return True
    
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # 1) Initialize data structure:
        uf = UnionFind(m*n)

        # 2) Set UF variables:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        lands = set()
        output = [0]

        # Iterate thru positions given:
        for row, col in positions:
            # Skip visited cells:
            if (row, col) in lands: 
                output.append(output[-1])
                continue

            # Initialized islands found:
            islands = output[-1]+1

            # Explore neighbors:
            for rd, cd in directions:
                r = row+rd
                c = col+cd
                
                if r in range(m) and c in range(n) and (r, c) in lands:
                    if uf.union(row*n+col, r*n+c): 
                        islands-=1 # One more island created
                        
            lands.add((row,col))
            output.append(islands)
            
        return output[1:]
