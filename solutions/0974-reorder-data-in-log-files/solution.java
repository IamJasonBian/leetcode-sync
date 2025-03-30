class Solution {
    public String[] reorderLogFiles(String[] logs) {
        String[][] letters = new String[logs.length][];
        String[] digits = new String[logs.length];
        int letterIndex = 0, digitIndex = 0;
        
        for (String s: logs) {
            int spacePos = s.indexOf(' ');
            boolean isDigit = Character.isDigit(s.charAt(spacePos + 1));
            
            if (isDigit) {
                digits[digitIndex++] = s;
            } else {
                letters[letterIndex++] = new String[] { s, s.substring(0, spacePos), s.substring(spacePos + 1) };
            }
        }

        Arrays.sort(letters, 0, letterIndex, (arg0, arg1) -> {
            int compare = arg0[2].compareTo(arg1[2]);
            if (compare == 0) {
                compare = arg0[1].compareTo(arg1[1]);
            }

            return compare;
        });

        int i, j = 0;
        for (i = 0; i < letterIndex; i++, j++) {
            logs[j] = letters[i][0];
        }

        for (i = 0; i < digitIndex; i++, j++) {
            logs[j] = digits[i];
        }

        return logs;
    }
}
