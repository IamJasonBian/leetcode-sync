class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Keep track of unmatched open parentheses
        stack = 0
        # Keep track of unmatched close parentheses
        extra_close = 0
        
        for char in s:
            if char == '(':
                # Add open parenthesis to stack
                stack += 1
            else:  # char == ')'
                if stack > 0:
                    # Match with existing open parenthesis
                    stack -= 1
                else:
                    # No matching open parenthesis available
                    extra_close += 1
        
        # Final answer is unmatched open + unmatched close
        return stack + extra_close
