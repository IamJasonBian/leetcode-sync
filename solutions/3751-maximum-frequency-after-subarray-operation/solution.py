class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        num_freq = defaultdict(int)
        total_k_cnt = 0
        for num in nums:
            if num == k:
                total_k_cnt += 1

        max_freq = 0
        cur_k_cnt = 0
        for num in nums:
            if num == k:
                cur_k_cnt += 1
                continue

            # one pass add/remove element but for max freq
            num_freq[num] = max(num_freq[num], cur_k_cnt) + 1
            max_freq = max(max_freq, num_freq[num]+total_k_cnt-cur_k_cnt)

        return max(max_freq, total_k_cnt)
            
        
