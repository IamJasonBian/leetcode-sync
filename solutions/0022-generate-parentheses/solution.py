class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
      
        
        output_ls = []
        
        def backtrack(output_ls, current_string, open ,close, max_s):
            if len(current_string) == max_s * 2:
                output_ls.append(current_string)
                return
            if(open < max_s):
                backtrack(output_ls, current_string + "(", open + 1, close, max_s)
            if(close < open):
                backtrack(output_ls, current_string + ")", open, close + 1, max_s)  
            

        backtrack(output_ls, "", 0, 0, n)
       
        return output_ls
