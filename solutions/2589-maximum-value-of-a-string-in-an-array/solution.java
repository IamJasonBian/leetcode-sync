class Solution {
    public int maximumValue(final String[] strs) {
        int result = 0;

        for(final String str : strs) {
            boolean isNumeric = true;

            for(int i = 0; i < str.length(); ++i) {
                if(!Character.isDigit(str.charAt(i))) {
                    isNumeric = false;
                    break;
                }
            }

            result = Math.max(result, isNumeric ? Integer.parseInt(str) : str.length());
        }

        return result;
    }
}
