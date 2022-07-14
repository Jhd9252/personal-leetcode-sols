class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    	"""
    	Using a 2 pointer approach to a sliding window method
    	Left pointer starts at index 0
    	The sliding window will expand to the right according to allowed changes
    	The sliding window will shift right according to allowed changes
		"""
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        # the right pointer iterates through after left pointer
        for r in range(len(s)):
        	# each time right pointer shifts, add 1 to the count of that letter in dictionary
            count[s[r]] = 1 + count.get(s[r], 0)
            # set maximum freq variable. Either stays the same, or the new updated letter from right shift
            maxf = max(maxf, count[s[r]])
            # if the length of the window - maxfreq is greater than allowed changes
            if (r - l + 1) - maxf > k:
            	# remove count from left pointer
                count[s[l]] -= 1
                # shift the left pointer
                l += 1
            # set res to max(current value, or window left)
            res = max(res, r - l + 1)
        return res