
class Solution {
        
    public int findUnsortedSubarray(int[] nums) {
   
        int left = 0;
        int right = nums.length - 1;
        

        while (left < nums.length - 1 && nums[left] <= nums[left + 1]) {
            left++;
        }
        
        
        if (left == nums.length - 1) {
            return 0;
        }
       
        while (right > 0 && nums[right] >= nums[right - 1]) {
            right--;
        }
        int subarrayMin = Integer.MAX_VALUE;
        int subarrayMax = Integer.MIN_VALUE;
        for (int i = left; i <= right; i++) {
            subarrayMin = Math.min(subarrayMin, nums[i]);
            subarrayMax = Math.max(subarrayMax, nums[i]);
        }
    
        while (left > 0 && nums[left - 1] > subarrayMin) {
            left--;
        }
        
        while (right < nums.length - 1 && nums[right + 1] < subarrayMax) {
            right++;
        }
        
        return right - left + 1;
    }}
