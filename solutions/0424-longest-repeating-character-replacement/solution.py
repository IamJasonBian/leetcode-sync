class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_size=0
        counter=collections.Counter()
        n=len(s)

        left=0
        for right in range(n):
            counter[s[right]]+=1
            while right-left+1-max(counter.values())>k:
                counter[s[left]]-=1
                left+=1
            max_size=max(max_size,right-left+1)
        
        return max_size
        
        
