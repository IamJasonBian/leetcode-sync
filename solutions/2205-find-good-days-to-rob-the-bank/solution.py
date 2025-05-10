class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        suffix = [0]*len(security)
        for i in range(len(security)-2, 0, -1): 
            if security[i] <= security[i+1]: suffix[i] = suffix[i+1] + 1
        
        ans = []
        prefix = 0
        for i in range(len(security)-time): 
            if i and security[i-1] >= security[i]: prefix += 1
            else: prefix = 0
            if prefix >= time and suffix[i] >= time: ans.append(i)
        return ans 
