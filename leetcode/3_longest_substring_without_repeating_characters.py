# -*- coding: utf-8 -*-
"""
Problem: Longest Substring without Repeating Characters

Given a string 's', find the length of the longet substring without repeating characters

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

Say we have string:
'abcdefgahi'
start index = 0
repeat index = 7
Then the length of current string without repeats is end - start
at that point, we want to keep the longest substring of substring without repeats
Keep track of each last seen index in 26 bucket map
"""
class Solution:
    # Runtime: O(n^2)
    # Space: O(26)
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            length = 1
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    longest = max(longest, length)
                    break
                else:
                    seen.add(s[j])
                    length += 1
        return longest

    # sliding window
    # track a map {char: last seen index}
    # if there is a repeating character, move the start position
    def lengthOfLongestSubstring(self, s: str) -> int:
        position = {}
        res = 0
        start = 0

        for end in range(len(s)):
            # check if char has been seen before
            if s[end] in position:
                # check if last known position is within current window
                # if it is, adjust to index + 1 else, outside position and less than start
                # therefore, take the larger index
                start = max(start, position[s[end]]+1)
            # no matter what, end position is now repeat free
            # record last known
            position[s[end]] = end
            # window is valid, current char is recorded
            # check the longest result
            res = max(res, end - start + 1)
        return res 

if __name__ == '__main__':
    alpha = Solution()
    s = 'pwwkew'
    print(alpha.lengthOfLongestSubstring(s))
    # wke, kew, 3
