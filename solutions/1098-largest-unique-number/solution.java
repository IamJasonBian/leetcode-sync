class Solution {
    public int largestUniqueNumber(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = n - 1; i >= 0; i--){
            if ((i==n-1 || nums[i] != nums[i+1]) && (i == 0 || nums[i] != nums[i-1])){
                return nums[i];
            }
        }
        return -1;
    }
}
