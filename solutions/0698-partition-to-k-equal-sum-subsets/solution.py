class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)
    
        total_array_sum = sum(arr)
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k
        arr.sort(reverse=True)
        taken = ['0'] * n
        memo = {}
        
        def backtrack(index, count, curr_sum):
            n = len(arr)
            taken_str = ''.join(taken)
            if count == k - 1:
                return True
            if curr_sum > target_sum:
                return False
            if taken_str in memo:
                return memo[taken_str]
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]
            
            for j in range(index, n):
                if taken[j] == '0':
                    taken[j] = '1'
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
                    taken[j] = '0'
                    
            memo[taken_str] = False
            return memo[taken_str] 
        
        return backtrack(0, 0, 0)
