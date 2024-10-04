class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int ans = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-2; i++) {
            int first = nums[i];
            int start = i+1;
            int end = nums.length-1;
            int sum;
            while (start<end){
                sum = first + nums[start] + nums[end];
                if(target>sum){
                    ans += (end-start);
                    start++;
                }else{
                    end--;
                }
            }
        }
        return ans;
    }
}
