

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        
        
        Arrays.sort(nums1);
        

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        

        for (int i = 0; i < nums2.length; i++) {
            maxHeap.offer(new int[]{nums2[i], i});
        }
        

        int left = 0;
        int right = nums1.length - 1;
        

        int[] result = new int[nums1.length];
        
       
        while (!maxHeap.isEmpty()) {
            

            int[] current = maxHeap.poll();
            int value = current[0];
            int index = current[1];
            
          
            if (nums1[right] > value) {
                
              
                result[index] = nums1[right];
                
      
                right--;
            } else {
                
                
                result[index] = nums1[left];
    
                left++;
            }
        }

        return result;
    }
}

