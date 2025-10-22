class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:

            '''

                Focus on two pointers and other approaches etc

            '''

            #for i in candidates:
            candidates.sort()
            res = []
            stack = [(0, [], 0)]

            while stack:
                idx, combination, current_sum = stack.pop()

                if current_sum == target:
                    res.append(combination[:])
                    continue

                if current_sum > target:
                    continue

                for i in range(idx, len(candidates)):
                    if i > idx and candidates[i] == candidates [i - 1]:
                        continue
                    if current_sum + candidates[i] > target:
                        break

                    stack.append((i+1, combination + [candidates[i]], current_sum + candidates[i]))
            return res

