class Solution {
    
    // Method to find the longest consecutive sequence
    public int longestConsecutive(TreeNode root) {
        
        // Start DFS from the root with initial length 0 and previous value as root's value minus one
        return dfs(root, null, 0);
    }
    
    // Helper method for DFS with memoization
    private int dfs(TreeNode node, Integer parentValue, int length) {
        
        // Base case: if the node is null, return the current length
        if (node == null) {
            return length;
        }
        
        // Check if the current node is consecutive
        length = (parentValue != null && node.val == parentValue + 1) ? length + 1 : 1;
        
        // Recursively find the longest path in the left and right subtrees
        int leftLength = dfs(node.left, node.val, length);
        int rightLength = dfs(node.right, node.val, length);
        
        // Return the maximum length found
        return Math.max(length, Math.max(leftLength, rightLength));
    }
}
