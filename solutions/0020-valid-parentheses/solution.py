class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        close_bracket = { '{':'}', '[':']', '(':')'}
        
        for char in s:
            if char in close_bracket:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if char == close_bracket[stack[-1]]:
                        stack.pop()
                    else:
                        return False
        return not stack
