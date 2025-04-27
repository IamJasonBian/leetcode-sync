
class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        
        int[] nonIncreasing = new int[security.length];
        int[] nonDecreasing = new int[security.length]; 

        for (int i=1; i<security.length; i++) {
            if (security[i] <= security[i-1]) {
                nonIncreasing[i] = nonIncreasing[i-1] + 1;
            } else {
                nonIncreasing[i] = 0;
            }
        }

        for (int i=security.length-2; i>=0; i--) {
            if (security[i] <= security[i+1]) {
                nonDecreasing[i] = nonDecreasing[i+1] + 1;
            } else {
                nonDecreasing[i] = 0;
            }
        }

        List<Integer> days = new ArrayList<>();

        for (int i=0; i<security.length; i++) {
            if ( nonDecreasing[i]>= time && nonIncreasing[i] >= time) {
                days.add(i);
            }
        }

        return days;
    }
}
