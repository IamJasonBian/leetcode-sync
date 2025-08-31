# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
     def pathSum(self, root: TreeNode, targetSum: int) -> int:

        # dictionary to store the prefix sums and their frequencies
        # subarray sum = k

        from collections import defaultdict

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1        

        if root is False:
            return 0

        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            count = prefix_sums.get(current_sum - targetSum, 0)

            # print("Current Line: ======= " + str(count))
            # print(current_sum - targetSum)
            # print(prefix_sums)

            prefix_sums[current_sum] += 1
            # print("Post Adjustment: ======= " + str(prefix_sums[current_sum]))
            
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # backtrack
            prefix_sums[current_sum] -= 1
            # prune for memory 
            if prefix_sums[current_sum] == 0:
               del prefix_sums[current_sum]

            return count

        return dfs(root, 0)


