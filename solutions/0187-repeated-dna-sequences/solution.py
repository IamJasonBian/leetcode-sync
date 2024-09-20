class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, output = set(), set()

        
        for start in range(n - L + 1):
            #backwards iteration

            #string manipulation from start : to start + L
            tmp = s[start : start + L]

            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output
