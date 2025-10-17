class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        stack = [("", 0, 0)]
        result = []
        while stack:
            s, o, c = stack.pop()
            if o == n and c == n:
                result.append(s)
                continue
            if o < n:
                stack.append((s + '(', o + 1, c))
            if c < o:
                stack.append((s + ')', o, c + 1))
        return result
