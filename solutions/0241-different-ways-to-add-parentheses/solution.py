class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        for i in range(len(expression)):
            char = expression[i]
            if char == '+' or char == '-' or char == '*':
                str1 = expression[:i]
                str2 = expression[i+1:]
                a = self.diffWaysToCompute(str1)
                b = self.diffWaysToCompute(str2)
                for x in a:
                    for y in b:
                        if char == '+':
                            result.append(x + y)
                        elif char == '-':
                            result.append(x - y)
                        elif char == '*':
                            result.append(x * y)
        if not result:
            result.append(int(expression))
        return result
