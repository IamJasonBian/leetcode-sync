
import java.util.Arrays;

class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        

        Arrays.sort(satisfaction);

        int totalSatisfaction = 0;
        int currentSum = 0;
        

        for (int i = satisfaction.length - 1; i >= 0; i--) {

            /* triangular dish ordering (satisfaction * time waiting)

            1 0 0 0 0 
            1 (2*2 = 4) 0 0 0
            1 (2*2 = 4) (2*3=6) 0 0

            vs

            1 (2*2 = 4) (2*4=8) 0 0     
                where do we put the 8 then?


            */
            currentSum += satisfaction[i];

            if (currentSum > 0) {
                totalSatisfaction += currentSum;
            } else {
                break;
            }
        }

        return totalSatisfaction;
    }
}

