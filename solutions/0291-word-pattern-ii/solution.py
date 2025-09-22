class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        len_p = len(pattern)
        len_s = len(s)
        self.res = False

        def backtrack(i, j, dic, rev_dic):
            if i == len_p and j == len_s:
                self.res = True
                return 
            elif i == len_p or j == len_s:
                return

            if pattern[i] not in dic:
                for l in range(1, len_s - j + 1):
                    word = s[j:j+l]
                    if word not in rev_dic:
                        dic[pattern[i]] = word
                        rev_dic[word] = pattern[i]
                        backtrack(i + 1, j + l, dic, rev_dic)
                        del dic[pattern[i]]
                        del rev_dic[word]

            elif pattern[i] in dic:
                word = dic[pattern[i]]
                k = j + len(word)
                
                if k <= len_s and s[j:k] == word:
                    backtrack(i + 1, k, dic, rev_dic)

        backtrack(0, 0, {}, {})
        
        return self.res

        
