   
class Solution {
   void swap(int[] nums, int i, int j)
   {
       int temp = nums[i];
       nums[i]= nums[j];
       nums[j]=temp;
   }
    public int maxScore(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int i=0,j=n-1;
        //Reversing the sorted array
        while(i<j)
        {
            swap(nums,i,j);
            i++;
            j--;
        }
       
        int count=0;
        // Making prefixSum long for managing overflow situation
        long prefixSum = 0;
        for(i=0;i<nums.length;i++)
        {
            prefixSum += nums[i];
            if(prefixSum>0)
                count++;

        }
        return count;
        
    }
}
