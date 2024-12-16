class Solution {
    public int[][] multiply(int[][] mat1, int[][] mat2) {
        int m = mat1.length;
        int k = mat1[0].length;
        int n = mat2[0].length;
        
        // Convert matrices to sparse representation
        Map<Integer, Integer>[] sparseRows = new Map[m];
        Map<Integer, Integer>[] sparseCols = new Map[n];
        
        // Initialize maps
        for (int i = 0; i < m; i++) {
            sparseRows[i] = new HashMap<>();
            for (int j = 0; j < k; j++) {
                if (mat1[i][j] != 0) {
                    sparseRows[i].put(j, mat1[i][j]);
                }
            }
        }
        
        for (int j = 0; j < n; j++) {
            sparseCols[j] = new HashMap<>();
            for (int i = 0; i < k; i++) {
                if (mat2[i][j] != 0) {
                    sparseCols[j].put(i, mat2[i][j]);
                }
            }
        }
        
        // Compute result
        int[][] result = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = dotProduct(sparseRows[i], sparseCols[j]);
            }
        }
        
        return result;
    }
    
    private int dotProduct(Map<Integer, Integer> vec1, Map<Integer, Integer> vec2) {
        if (vec2.size() < vec1.size()) {
            var tmp = vec1;
            vec1 = vec2;
            vec2 = tmp;
        }
        int product = 0;
        for (var entry : vec1.entrySet()) {
            product += vec2.getOrDefault(entry.getKey(), 0) * entry.getValue();
        }
        return product;
    }
}
