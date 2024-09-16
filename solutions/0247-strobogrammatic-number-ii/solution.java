public class Solution {
    public List<String> findStrobogrammatic(int n) {
        List<String> cur, ans;
        ans = new ArrayList<String>((n & 1) == 0 ? Arrays.asList("") : Arrays.asList("0", "1", "8"));
        if (n < 2) return ans;
        
        for (;n > 1; n -= 2) {
            cur = ans;
            ans = new ArrayList<String>();
            for (String i : cur) {
                if (n > 3) ans.add('0' + i + '0');
                ans.add('1' + i + '1');
                ans.add('8' + i + '8');
                ans.add('6' + i + '9');
                ans.add('9' + i + '6');
            }
        }
        
        return ans;
    }
}
