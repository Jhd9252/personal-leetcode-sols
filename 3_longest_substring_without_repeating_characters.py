# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 3. Longest Substring Without Repeating Characters
Test Cases: 987 / 987 test cases passed.
Runtime: 67 ms (runtime beats 85.06 % of python3 submissions)
Memory Usage: 14.2 MB (memory usage beats 16.14 % of python3 submissions.)


Given a string s, find the length of the longest substring without repeating characters.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # will be using pointers and dictionary
        # the used characters: last used index
        used = {}
        # set left bound
        left = 0
        width = 0
        
        # iterate the right pointer
        for right in range(len(s)):
            # if the char at the right bound hasn't been used yet
            if s[right] not in used:
                # we will set width to the max of either the current window, 
                # or this new window between left and right bounds
                width = max(width, right - left + 1) 
            # else if the char at right bound is already used
            else:
                # if the char has been used 0 times
                if used[s[right]] < left:
                    # set the width to max of either current or new window
                    width = max(width, right - left + 1)
                # else the char has been used >= 1 times
                else:
                    # move left bound to current right bound
                    left = used[s[right]] + 1
            # set new dictionary entry
            used[s[right]] = right
        return width
        
alpha = Solution()
s = 'pwwkew'
print(alpha.lengthOfLongestSubstring(s))