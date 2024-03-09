class Solution:
    def checkValidString(self, s: str) -> bool:
        left_c, right_c = 0, 0

        for c in s:
            if c == "(":
                left_c, right_c = left_c + 1, right_c + 1
            elif c == ")":
                left_c, right_c = left_c - 1, right_c - 1
            else:
                left_c, right_c = left_c -1, right_c + 1
                
            if right_c < 0:

                return False
                
            if left_c < 0:
                left_c = 0
        return left_c == 0
