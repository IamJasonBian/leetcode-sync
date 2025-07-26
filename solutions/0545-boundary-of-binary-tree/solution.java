import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        result.add(root.val);
        
        // Add left boundary (excluding leaf node)
        addLeftBoundary(root.left, result);
        
        // Add leaves (left to right)
        addLeaves(root.left, result);
        addLeaves(root.right, result);
        
        // Add right boundary (excluding leaf node)
        addRightBoundary(root.right, result);
        
        return result;
    }
    
    private void addLeftBoundary(TreeNode node, List<Integer> result) {
        if (node == null || (node.left == null && node.right == null)) return;
        result.add(node.val);
        if (node.left != null) {
            addLeftBoundary(node.left, result);
        } else {
            addLeftBoundary(node.right, result);
        }
    }
    
    private void addRightBoundary(TreeNode node, List<Integer> result) {
        if (node == null || (node.left == null && node.right == null)) return;
        if (node.right != null) {
            addRightBoundary(node.right, result);
        } else {
            addRightBoundary(node.left, result);
        }
        result.add(node.val);
    }
    
    private void addLeaves(TreeNode node, List<Integer> result) {
        if (node == null) return;
        if (node.left == null && node.right == null) {
            result.add(node.val);
            return;
        }
        addLeaves(node.left, result);
        addLeaves(node.right, result);
    }
}
