class Solution:
    def combo(self, result, candidates, target, start, path):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return result
        for i in range(start, len(candidates)):
            self.combo(result, candidates, target-candidates[i], i, path+[candidates[i]])

    def combinationSum(self, candidates, target):
        result = []
        self.combo(result, candidates, target, 0, [])
        return result
