class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        '''
            You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1]

            Naively, I would just iterate and replace each via list indexing
                
                Why wouldn't one-pass indexing work here 

                * Do Runtime - there's is two scans so O(mxn)
                * Space: O(1)

                Rather than scan we can store the last hash

        '''


        pos = {val: i for i, val in enumerate(nums)}
        #index based (vs number based)

        for i in range(len(operations)):
            old_val = operations[i][0]
            new_val = operations[i][1]
            idx = pos[old_val]
            nums[idx] = new_val
            del pos[old_val]
            pos[new_val] = idx

        return nums 

