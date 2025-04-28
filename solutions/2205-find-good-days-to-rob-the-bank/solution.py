class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))
        
        non_increasing = [False] * n
        dec_len = 1
        
        # First pass: Check non-increasing condition
        for idx in range(1, n):
            if security[idx-1] >= security[idx]:
                if dec_len >= time:
                    non_increasing[idx] = True
                dec_len += 1
            else:
                dec_len = 1
        
        inc_len = 1
        good_days = []
        
        # Second pass: Check non-decreasing condition
        for idx in range(n-2, -1, -1):
            if security[idx] <= security[idx + 1]:
                if inc_len >= time and non_increasing[idx]:
                    good_days.append(idx)
                inc_len += 1
            else:
                inc_len = 1
        
        return good_days
