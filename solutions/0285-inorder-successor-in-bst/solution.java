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
    TreeNode succ;
    boolean found;
    int target;

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        target = p.val;
        inorder(root);
        return succ;
    }

    void inorder(TreeNode root){
        if(root == null || succ != null){
            return;
        }
        if(target < root.val){
            inorder(root.left);
        }

        if(succ != null){
            return;
        }
        if(found){
            succ = root;
        }
        else if(root.val == target){
            found = true;
        }

        inorder(root.right);
    }
}
