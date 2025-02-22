
class Solution {
    public boolean isConsecutive(int[] nums) {

        if (nums == null || nums.length == 0) {
            return false;
        }
        HashSet<Integer> uniqueNums = new HashSet<>();

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        // Bounds should line up here
        for (int num : nums) {
            uniqueNums.add(num);
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        // Check if the number of unique elements matches the expected count
        return uniqueNums.size() == nums.length && max - min + 1 == nums.length;
    }
}
