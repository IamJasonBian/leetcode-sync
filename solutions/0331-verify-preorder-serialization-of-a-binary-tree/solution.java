/*
 * This solution uses a Stack Simulation algorithm to verify the preorder serialization of a binary tree.
 * The algorithm simulates the process of filling slots in a binary tree. Each node occupies one slot but creates two new slots.
 * A null node ('#') occupies one slot without creating any new slots.
 * The process is valid if all slots are filled exactly by the end of the traversal.
 */

class Solution {
    public boolean isValidSerialization(String preorder) {
        String[] nodes = preorder.split(",");
        int slots = 1;
        for (String node : nodes) {

            slots--;
            if (slots < 0) {
                return false;
            }
            if (!node.equals("#")) {
                slots += 2;
            }
        }
        return slots == 0;
    }
}

