class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s.lower()) == sorted(t.lower())
        return Counter(s.lower()) == Counter(t.lower())
