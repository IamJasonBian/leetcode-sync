import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        // Step 1: Intervals ko unke start time ke basis pe sort karo
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        
        List<int[]> mergedIntervals = new ArrayList<>();

        
        for (int[] current : intervals) {

            if (mergedIntervals.isEmpty() || mergedIntervals.get(mergedIntervals.size() - 1)[1] < current[0]) {
                mergedIntervals.add(current);
            } 
            else {
                int[] lastInterval = mergedIntervals.get(mergedIntervals.size() - 1);
                lastInterval[1] = Math.max(lastInterval[1], current[1]);
            }
        }

        
        return mergedIntervals.toArray(new int[mergedIntervals.size()][]);
    }
}
