class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prod = 1;
        int nonZeroProd = 1;
        int zeroCount = 0;
        for(int i = 0; i < nums.length; i++) {
            prod *= nums[i];
            if(nums[i] != 0)
                nonZeroProd *= nums[i];
            else
                zeroCount++;
        }    
        
        int[] result = new int[nums.length];
        if(zeroCount > 1) return result;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0)
                result[i] = prod/nums[i];
            else
                result[i] = nonZeroProd;
        }
        
        return result;
    }
}


