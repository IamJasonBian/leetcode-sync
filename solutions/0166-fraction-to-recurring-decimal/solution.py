class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
            
        # Handle signs
        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Get integer part
        integer = numerator // denominator
        numerator = numerator % denominator
        
        if numerator == 0:
            return sign + str(integer)
            
        # Get decimal part
        decimal = []
        seen = {}  # remainder -> position
        position = 0
        
        while numerator and numerator not in seen:
            seen[numerator] = position
            numerator *= 10
            decimal.append(str(numerator // denominator))
            numerator %= denominator
            position += 1
            
        # If there's a repeating part
        if numerator:
            repeat_start = seen[numerator]
            decimal.insert(repeat_start, '(')
            decimal.append(')')
            
        return sign + str(integer) + '.' + ''.join(decimal)
