class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        i, j = 0, 0

        while i < n and j < n:
            while i < n and pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            
            if i < n:
                stack.append(pushed[i])
                i += 1
            
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return len(stack) == 0
