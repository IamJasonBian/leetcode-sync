class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        seen = {}
        left = 0
        max_length = 0
        max_freq = 0

        for right in range(len(s)):
            char = s[right]
            seen[char] = seen.get(char, 0) + 1
            max_freq = max(max_freq, seen[char])
            window_size = right - left + 1
            if window_size - max_freq > k:
                seen[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

