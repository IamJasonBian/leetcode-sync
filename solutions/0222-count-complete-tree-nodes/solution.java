class Solution {
  public int countNodes(TreeNode root) {
    return root != null ? 1 + countNodes(root.right) + countNodes(root.left) : 0;
  }
}

// binary search works here because the total number of nodes expands as we go down in the tree 
