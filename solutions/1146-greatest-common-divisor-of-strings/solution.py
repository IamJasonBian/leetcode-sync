class Solution:
    def gcdOfStrings(self, str1, str2):

        # Recursive implementation

        # If str1 length is less than that of str2 then recur with gcd(str2, str1)
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        
        # If str1 is not the concatenation of str2
        elif not str1.startswith(str2):
            return ""
        
        # If str2 is empty, str1 is the GCD string
        elif len(str2) == 0:
            return str1
        
        # Cut off the common prefix part of str1 & then recur (prefix based implementation)
        else:
            return self.gcdOfStrings(str1[len(str2):], str2)
