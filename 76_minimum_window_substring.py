"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # left and right pointers solution with hashmaps and sliding window
        # expand window by shifting right pointer until valid
        # contract window by shifting left pointer until not valid
        # record the minimum valid subwindow

        # Define variables
        # this is how we will compare
        s_count, t_count = Counter(), Counter(t)
        
        l, r = 0, 0
        
        results = []
        
        # loop until right pointer reaches the end of string
        while r <= len(s)-1:
                                    
            # Find valid window
            #  add character to dictionary += 1 
            s_count[s[r]] += 1            
            # shift the right pointer += 1
            r += 1

            # keep expanding the window until == t dictionary
            if s_count & t_count != t_count:
                continue
                
            # otherwise, we will contract the window until it is no longer valid
            # Minimize this window
            # loop until l reaches r, or window is not valid
            while l < r:
                # update s_count dictionary
                s_count[s[l]] -= 1 
                # shift left pointer += 1
                l += 1
                # continue shifting left pointer until window is no longer valid
                if s_count & t_count == t_count:
                    continue
                # otherwise, the previous window is currently the smallest, and valid
                # append to results array
                results.append(s[l-1:r])
                break
            
            
        # Return result
        # if results is empty (from length or t not in s), return empty string
        if not results:
            return ""        
        # otherwise, return the minimum substring recorded from loop
        return min(results, key=len)





        