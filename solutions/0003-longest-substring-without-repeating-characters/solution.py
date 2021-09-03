class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		start = -1    # start index of sliding window
		max_length = 0       # the longest substring length
		d = {}        # store non-repeating characters in sliding window 

		for i in range(len(s)):     

			if s[i] in d and d[s[i]] > start:
				start = d[s[i]]
				d[s[i]] = i

			else: #s[i] not in d
				d[s[i]] = i

				if i - start > max_length:  # (i - start) is the length of sliding window  
					max_length = i-start

		return max_length
