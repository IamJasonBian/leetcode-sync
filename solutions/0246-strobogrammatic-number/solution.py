class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated_string_builder = []
        for c in reversed(num):
            if c in {'0', '1', '8'}:
                rotated_string_builder.append(c)
            elif c == '6':
                rotated_string_builder.append('9')
            elif c == '9':
                rotated_string_builder.append('6')
            else: 
                return False

        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num
