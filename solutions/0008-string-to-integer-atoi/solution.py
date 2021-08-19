class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :return: int
        """
        if len(s) == 0:
            return 0
        elif s[0].isalpha():
            return 0
        ans = ""
        for c in s:
            if c.isdigit() or c == '.' or c == '-' or c == '+' or c == ' ':
                ans += c
            elif c.isalpha():
                break
        ans = ans.strip()
        anssize = len(ans)
        if anssize == 0:
            return 0
        for i in range(anssize):
            v = ans[i]
            if i > 0 and (v == '+' or v == '-' or v == ' '):
                ans = ans[0:i]
                break
        if (ans[0] == '-' or ans[0] == '+') and len(ans) == 1:
            return 0
        val = int(float(ans))
        if val >= 2147483647:
            val = 2147483647
        elif val < -2147483647:
            val = -2147483648
        return val
