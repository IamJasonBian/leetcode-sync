var diameterOfBinaryTree = function(root) {
    let maxDiameter = 0;  // Track maximum diameter found
    
    function dfs(node) {
        // Base case: null node has height -1 to make leaf nodes have diameter 0
        if (node === null) return -1;
        
        // Get heights of left and right subtrees
        const leftHeight = dfs(node.left);
        const rightHeight = dfs(node.right);
        
        // Update max diameter if current node's path is longer
        // Diameter at current node = leftHeight + rightHeight + 2
        maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight + 2);
        
        // Return height of current node
        return Math.max(leftHeight, rightHeight) + 1;
    }
    
    dfs(root);
    return maxDiameter;
};
