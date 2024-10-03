class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int minLength = Math.min(s.length(), t.length());

        int p = 0;
        int q = 0;
        boolean wasDeleted = false;

        for (int i = 0; i < minLength; i++) {
            if (s.charAt(p) == t.charAt(q)) {
                p++;
                q++;
                continue;
            }
            return isOneDistance(s, t, p + 1, q + 1)
                    || isOneDistance(s, t, p, q + 1)
                    || isOneDistance(s, t, p + 1, q);
        }

        return Math.abs(s.length() - t.length()) == 1;
    }
    
    private boolean isOneDistance(String s, String t, int p, int q) {
        while (p < s.length() && q < t.length()) {
            if (s.charAt(p) != t.charAt(q)) {
                return false;
            }
            p++;
            q++;
        }

        return p == s.length() && q == t.length();  
    }    
}
