class Solution {
    private static final int DISTINCT_THRESHOLD = 2;
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> mapCount = new HashMap<>();
        int distinctCharCount = 0;
        int l = 0;
        int r = 0;
        int maxLen = 0;
        while (r < s.length()) {
            var ch = s.charAt(r);
            mapCount.put(ch, mapCount.getOrDefault(ch, 0) + 1);
            if (mapCount.get(ch) == 1) {
                distinctCharCount++;
            }
            while (l < r && distinctCharCount > DISTINCT_THRESHOLD) {
                var leftCh = s.charAt(l);
                mapCount.put(leftCh, mapCount.get(leftCh) - 1);
                if (mapCount.get(leftCh) == 0) {
                    distinctCharCount--;
                }
                ++l;
            }
            maxLen = Math.max(maxLen, r - l + 1);
            ++r;
        }
        return maxLen;
    }
}
