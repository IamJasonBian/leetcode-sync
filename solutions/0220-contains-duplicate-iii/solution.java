class Solution {
    public boolean sum(int[] nums,int k,int valueDiff){
        int i=0;int j=k; int n =nums.length;
        while(j<n){
            if(Math.abs(nums[i]-nums[j])<=valueDiff) return true;
            i++;
            j++;
        }
        return false;
    }
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        if(valueDiff ==0){
            HashMap<Integer,Integer> map = new HashMap<>();
            for(int i=0;i<nums.length;i++){
                if(map.containsKey(nums[i])){
                    if(Math.abs(map.get(nums[i])-i)<=indexDiff) return true;
                }
                map.put(nums[i],i);
            }
            return false;
        }
        int j=indexDiff; int n = nums.length;boolean ss= false;
        for(int k=1;k<=j;k++){
            ss = sum(nums,k,valueDiff);
            if(ss == true) return true;
        }
        return false;
    }
}
