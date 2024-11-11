class Solution {
    public int sum(int num1, int num2) {
        int res = 0;
        while (num1 != 0) {
            res += inc(num1);
            num1 -= inc(num1);
        }
        while (num2 != 0) {
            res += inc(num2);
            num2 -= inc(num2);
        }
        return res;
    }
    
    private int inc(int num) {
        return num > 0 ? 1 : -1;
    }
}

