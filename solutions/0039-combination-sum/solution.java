import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        find(res, new ArrayList<>(), candidates, target, 0);
        return res;
    }

    void find(List<List<Integer>> res, List<Integer> temp, int[] nums, int target, int st) {
        if (target < 0) {
            return; // Stop exploration if the target goes negative
        }
        if (target == 0) {
            res.add(new ArrayList<>(temp)); // Add valid combination to the result
            return;
        }
        for (int i = st; i < nums.length; i++) {
            temp.add(nums[i]); // Choose the number
            find(res, temp, nums, target - nums[i], i); // Explore further with updated target and same index
            temp.remove(temp.size() - 1); // Backtrack to explore other combinations
        }
    }
}
