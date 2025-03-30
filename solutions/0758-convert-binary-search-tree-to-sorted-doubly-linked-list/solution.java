class Solution {
    Node prev;
    Node head;
    public Node treeToDoublyList(Node root) {
        if(root ==null){
            return null;
        }
        prev = null;
        head = null;
        helper(root);
        prev.right = head;
        head.left = prev;
        return head;
    }

    public void helper(Node root){
        if(root ==null){
            return ;
        }
        helper(root.left);
        if(prev==null){
            prev = root;
            head = root;
        } else {
            prev.right = root;
            root.left = prev;
            prev = root;
        }
        helper(root.right);

    }
}
