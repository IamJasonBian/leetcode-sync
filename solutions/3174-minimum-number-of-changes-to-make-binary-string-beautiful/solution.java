class Solution {

    public int minChanges(String s) {
        // Initialize with first character of string
        char currentChar = s.charAt(0);

        int consecutiveCount = 0;
        int minChangesRequired = 0;

        // Iterate through each character in the string
        for (int i = 0; i < s.length(); i++) {
            // If current character matches the previous sequence
            if (s.charAt(i) == currentChar) {
                consecutiveCount++;
                continue;
            }

            if (consecutiveCount % 2 == 0) {
                consecutiveCount = 1;
            }
            else {
                consecutiveCount = 0;
                minChangesRequired++;
            }
            currentChar = s.charAt(i);
        }

        return minChangesRequired;
    }
}
