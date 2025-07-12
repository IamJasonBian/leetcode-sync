class Solution {
    public int wiggleMaxLength(int[] nums) {
        int count = 1;
        int prev = 0;
        for(int i = 1 ; i < nums.length ; i++)
        {
            int curr = nums[i] - nums[i - 1];
            if((curr > 0 && prev <= 0) || (curr < 0 && prev >= 0))
            {
                count++;
                prev = curr;
            }
        }
    return count;}
}
