class Solution:
    def customSortString(self, order: str, s: str) -> str:


        '''

        You are given two strings order and s. All the characters of order are unique and where sorted in some customer order previously. 

        Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before character y in order, then x should occur before y in the permuted string.

        Return any permutation of s that satisfies this property

        '''
        l=len(s)
        ans=''
        for i in order:
            if i in s:
                c=s.count(i)
                ans+=(i)*c
        for i in s:
            if i not in ans:
                c=s.count(i)
                ans+=(i)*c
        return ans

