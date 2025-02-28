class Solution {
    
    //Get counts of each letter.
    int[] getCount(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); ++i)
            count[s.charAt(i) - 'a']++;
        return count;
    }
    
    boolean canS2BreakS1(int[] s1, int[] s2) {
        int p1 = 0, p2 = 0;
        while (p1 < 26 && p2 < 26) {
            //No remaining characters for this letter in S1. Move on to the next.
            if (s1[p1] == 0)
                ++p1;
            //The characters in S2 need to be at least as large as that in S1. If not, move to next.
            else if (p1 > p2 || s2[p2] == 0)
                ++p2;
            else {
                //We matched characters in S1 with the smallest characters in S2 that are greater than or equal to them. 
                int diff = Math.min(s1[p1], s2[p2]);
                s1[p1] -= diff;
                s2[p2] -= diff;
            }
        }
        
        int sum = 0;
        for (int i = 0; i < 26; ++i)
            sum += s1[i] + s2[i];
        
        //No characters should be left unmatched.
        return sum == 0;
    }
    
    public boolean checkIfCanBreak(String s1, String s2) {
        int[] s1Count = getCount(s1), s2Count = getCount(s2);
        return canS2BreakS1(s1Count.clone(), s2Count.clone()) || canS2BreakS1(s2Count, s1Count);
    }
}
