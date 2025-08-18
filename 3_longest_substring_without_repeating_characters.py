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
        '''
        Brute Force Approach: Treat each index as a starting point
        runtime O(N**2)
        Space : O(N) to track the characters seen
        '''
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

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding Window: 
        A. We track each last seen index per character. 
        B. If there is a repeating character, to make the window valid, we move left = lastPos + 1
        '''
        pos = {}
        res = 0
        left = 0
        for right in range(len(s)):
            # repeat
            if s[right] in pos:
                # The repeated character may be outside our current window
                # Thus, we want the max, which is guaranteed to be in window
                left = max(left, pos[s[right]] + 1)
            pos[s[right]] = right
            res = max(res, right - left + 1)
        return res
        
        
                
        
        
alpha = Solution()
s = 'pwwkew'
print(alpha.lengthOfLongestSubstring(s))