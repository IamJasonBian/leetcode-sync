from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = []
        char= {}
    
        for i in arr:
            if i in char:
                char[i] += 1
            else:
                char[i] = 1

        for key, value in char.items():
            if value == 1:
                ans.append(key)

        if k > len(ans):
            return str("")
        else:
            return str(ans[k-1])


