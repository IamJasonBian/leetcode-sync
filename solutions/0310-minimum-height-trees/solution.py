class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        '''

            A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

            We want to find the right permutation height-wise for the tree 

            Brute-Force [0]

            (Math? Approach)

                * Permutation of all the trees
                * Find the shortest tree 
                * Each direction really only lines one-way etc

            Can you come up with a test case that has "two" middles? 

            [[1,0],[1,2],[1,3]] - here 1 3 and 3 1 are fundamentally the same 

            Math Based Approach 

            Find the "middle" and measure x edges Out. The longest "edge" is the depth etc 

            "Leaf Pruning"

            "Count the process of leaf pruning" 

        '''

        pass

        g = [set() for _ in range(n)]
      
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        '''

        {0, 2, 3} _ maps to 1 

        [{1}, {0, 2, 3}, {1}, {1}]

        '''
        if n == 0:
            return []
        if len(edges) < 1:
            return [0]

        print(g)
        leaves = [i for i in range(n) if len(g[i]) == 1]
        print(leaves)

        while n > 2:
            n -= len(leaves)
            new = []
            for u in leaves:
                v = next(iter(g[u]))
                g[v].remove(u)
                if len(g[v]) == 1:
                    new.append(v)
                g[u].clear()
            leaves = new
        return leaves


        
                    






