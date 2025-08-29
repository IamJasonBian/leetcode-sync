import java.util.Arrays;

class Solution {
    public int countDays(int days, int[][] m) {
        if (m.length == 0) return days;
        
        Arrays.sort(m, (a, b) -> a[0] - b[0]);
        int last = 0, res = 0;
        
        for (int[] meet : m) {
            if (meet[0] > last + 1) res += meet[0] - last - 1;
            last = Math.max(last, meet[1]);
            if (last >= days) return res;
        }
        
        return res + Math.max(days - last, 0);
    }
}
