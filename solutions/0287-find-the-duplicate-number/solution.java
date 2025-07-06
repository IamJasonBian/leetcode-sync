public class Solution {
	int hashes=5;
	int bits=5000000;
	int[] primes = {31, 37,  41,  43, 47, 53, 59, 61, 67, 71};
    
    public int findDuplicate(int[] nums) {
        
        boolean[] bitsMasks = new boolean[bits];



        // bloom filter: 
        for(int i=0; i<nums.length; i++){
        	int count=0;
            for(int h=0; h<hashes; h++){
            	String s =Integer.toString(nums[i]);
                int hash = 0;
                for(int c=0; c<s.length();c++)
                	hash = primes[h]*hash + s.charAt(c);
                hash =  hash % bits;
                if(hash<0)
                	hash = ( bits + hash) %bits;
                if(!bitsMasks[hash])
                	count++;
                bitsMasks[hash]=true;
            }
            if (count==0)
            	return nums[i];
        }       
        return -1;
    }
}
