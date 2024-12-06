class Solution(object):
    def minOperations(self, logs):
        ans = 0
        for s in logs:
            if s == "../" and ans: ans -= 1
            elif s != "./" and s != "../": ans += 1
        return ans
