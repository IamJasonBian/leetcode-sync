class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        map = {}
        strs = s.split(" ")
        print(strs)
        check = set(strs)
        if len(pattern) != len(strs):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map:
                map[pattern[i]] = strs[i]
            elif map[pattern[i]] != strs[i]:
                return False
        

        if len(check) == len(map):
            return True
        else:
            return False
        
        
