from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def normalize(s):
            if not s:
                return s
            shift = ord(s[0]) - ord('a')

            # Since first value is linked to every other value after etc
            return ''.join(
                chr((ord(c) - shift) % 26 + ord('a')) 
                for c in s
            )

        normalizedGroups = defaultdict(list)
        for s in strings:

            # put the shifts into normalizedGroups
            # we run shift after the initial anchor
            normalizedGroups[normalize(s)].append(s)
                # 'tuv': ['abc', 'bcd', 'xyz'] (what is this normalization?)

            '''
            
            ord("a") = 97 
            shift = 0 

            97 - 0 % 26 + ord('a') = 

                = 97 + 97
                = 'u' value



            normalizedGroups = {
            'tuv': ['abc', 'bcd', 'xyz'],   # These strings normalize to "tuv"
            'tvxy': ['acef'],               # This string normalizes to "tvxy"
            'ts': ['az', 'ba']              # These strings normalize to "ts"
                    }

            crux: Strings with same relative character        distances map to same normalized form

            shift = ord('b') - ord('a') = 1
            'b' -> 't' ((98-1) % 26 + ord('t'))
            'c' -> 'u' ((99-1) % 26 + ord('u'))
            'd' -> 'v' ((100-1) % 26 + ord('v'))
            normalizes to: "tuv"
            
            '''
        return list(normalizedGroups.values())
