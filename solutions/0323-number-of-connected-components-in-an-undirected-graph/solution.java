class Solution {
    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];
        int[] size = new int[n];
        
        // Initialize DSU
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        
        int components = n;
        
        for (int[] edge : edges) {
            components -= union(parent, size, edge[0], edge[1]);
        }
        
        return components;
    }
    
    private int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]); // Path compression
        }
        return parent[x];
    }
    
    private int union(int[] parent, int[] size, int x, int y) {
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        
        if (rootX == rootY) return 0; // Already connected
        
        // Union by size: smaller tree gets attached to larger tree
        if (size[rootX] < size[rootY]) {
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        } else {
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
        }
        
        return 1; // Reduced components by 1
    }
}
