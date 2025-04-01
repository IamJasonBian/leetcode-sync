class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        max_length = 0  

        '''

            strings: s and t
                new string: select a substring from s and a substring from t, then concatenating them in order

            Return the length of the longest palindrome that can be formed

        '''

        
        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                s_substr = s[i:j]
                for k in range(len(t) + 1):
                    for l in range(k, len(t) + 1):
                        
                        t_substr = t[k:l]
                        concat = s_substr + t_substr
                        
                        if concat == concat[::-1] and len(concat) > 0:
                            max_length = max(max_length, len(concat))
        return max_length
