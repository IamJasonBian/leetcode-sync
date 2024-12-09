class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def parse():
            nonlocal i
            lst = NestedInteger()
            while i < len(s):
                prev = i
                while s[i] == '-' or s[i].isdigit():
                    i += 1
                if prev != i:
                    lst.add(NestedInteger(int(s[prev:i]))) # parse a number
                elif s[i] == '[':
                    i += 1
                    lst.add(parse()) # add a new list
                elif s[i] == ']': # return processed list
                    i += 1
                    return lst
                else: # for now it's just ','
                    i += 1
            return lst
        i = 1
        return parse() if s[0] == '[' else NestedInteger(int(s)) # parse a number or a list
