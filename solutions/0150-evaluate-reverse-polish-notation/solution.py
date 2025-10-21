class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Tokens is already split *
        token_set = {"+", "-", "*", "/"}
        eval_block = []
        res = 0

        #while len(tokens) > 0:
        for i in tokens:
            if i not in token_set:
                
                #take two elements out 

                eval_block.append(int(i))
               
                #print(eval_block)
            else:
                eval = int(eval_block.pop())
                if i == '+':
                    eval_block[-1] =  eval_block[-1] + int(eval)
                elif i == '-':
                    eval_block[-1] = eval_block[-1] - int(eval)
                elif i == '*':
                    eval_block[-1] = eval_block[-1] * int(eval) 
                elif i == '/':    
                    eval_block[-1] = int(eval_block[-1] / int(eval))
        #print(res)
        #print(eval_block)
        return eval_block[0]
        

