public class TreeNode {
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
    private String smallestLeafString = "";

    public String smallestFromLeaf(TreeNode root) {
        dfs(root, new StringBuilder());
        return smallestLeafString;
    }

    private void dfs(TreeNode node, StringBuilder path) {
        if (node == null) return;
        path.append((char)('a' + node.val));
        if (node.left == null && node.right == null) {
            String pathReversed = path.reverse().toString();
            if (smallestLeafString.isEmpty() || pathReversed.compareTo(smallestLeafString) < 0) {
                smallestLeafString = pathReversed;
            }
            path.reverse(); // Reverse the path back for backtracking
        }
        dfs(node.left, path);
        dfs(node.right, path);
        path.deleteCharAt(path.length() - 1); // Remove the current node's character for backtracking
    }
}

