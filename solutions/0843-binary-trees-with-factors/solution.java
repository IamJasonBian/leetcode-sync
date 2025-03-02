
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
    Arrays.sort(arr);
        
        
        
        Map<Integer, Long> treeCountMap = new HashMap<>();
         
        long mod = 1_000_000_007;
        
        for (int i = 0; i < arr.length; i++) {
            
            long count = 1;
            
            for (int j = 0; j < i; j++) {
                
                if (arr[i] % arr[j] == 0) {
                    int otherFactor = arr[i] / arr[j];
                    
                   
                    if (treeCountMap.containsKey(otherFactor)) {
                        count += treeCountMap.get(arr[j]) * treeCountMap.get(otherFactor);
                        count %= mod;
                    }
                }
            }

            treeCountMap.put(arr[i], count);
        }
        

        long totalTrees = 0;
        for (long value : treeCountMap.values()) {
            totalTrees += value;
            totalTrees %= mod;
        }
    

        return (int) totalTrees;
    }
}
