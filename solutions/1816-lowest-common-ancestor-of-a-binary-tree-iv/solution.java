/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        ArrayList<Integer> nodeValues = new ArrayList<>();
        for (TreeNode node : nodes) {
            nodeValues.add(node.val);
        }
        
        ArrayList<TreeNode> ancestors = new ArrayList<>();
        findMatchingNodes(root, nodeValues, ancestors);
        
        return ancestors.isEmpty() ? null : ancestors.get(0);
    }
    
    private int findMatchingNodes(TreeNode root, ArrayList<Integer> targetValues, ArrayList<TreeNode> ancestors) {
        if (root == null) {
            return 0;
        }
        
        int matchCount = 0;
        
        // Count matching nodes in left and right subtrees
        matchCount += findMatchingNodes(root.left, targetValues, ancestors);
        matchCount += findMatchingNodes(root.right, targetValues, ancestors);
        
        // Check if current node is a target
        if (targetValues.contains(root.val)) {
            matchCount++;
        }
        
        // If we've found all target nodes, this could be the LCA
        if (matchCount == targetValues.size()) {
            ancestors.add(root);
        }
        
        return matchCount;
    }
}
