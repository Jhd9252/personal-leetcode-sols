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
        '''
        Brute Force: Treat every index as a starting point
        Runtime: O(s*t)
        Space: O(26) -> O(1)
        '''
        res = ''
        for i in range(len(s)):
            truth = collections.Counter(t)
            for j in range(i, len(s)):
                if s[j] not in truth:
                    continue
                truth[s[j]] -= 1
                if all(truth[x] <= 0 for x in truth):
                    if res == '': res = s[i:j+1]
                    else: res = min(res, s[i:j+1], key = len)
        return res
    def minWindow(self, s: str, t: str) -> str:
        '''
        Sliding Window:
        Runtime: O(n + m)
        Space: O(26) -> O(1)
        '''
        s_count, t_count = Counter(), Counter(t)
        l, r = 0, 0
        results = []
        while r <= len(s)-1:                
            s_count[s[r]] += 1            
            r += 1
            if s_count & t_count != t_count:
                continue

            while l < r:
                s_count[s[l]] -= 1 
                l += 1
                if s_count & t_count == t_count:
                    continue
                results.append(s[l-1:r])
                break
        if not results:
            return ""        
        return min(results, key=len)

    

    def minWindow(self, s:str, t:str) -> str:
        '''
        Sliding Window with char array (two pointer)
        '''

        # exceptions
        if not s or not t or len(t) > len(s):
            return ''

        # map of 128 possible chars 
        mapper = [0] * 128

        # increment counts of t only
        for i in range(len(t)):
            mapper[ord(t[i]) - ord('A')] += 1

        left, right = 0, 0 
        res = ''
        minLength = float('inf')
        count = len(t) # fast lookup of our count, only move if touches boundary

        # starting at 0, 0 -> increment right 
        while right < len(s):

            # if the current letter exists in t, and is > 0: 
            # then we do not have a full count, decrement count
            if mapper[ord(s[right])- ord('A')] > 0:
                count -= 1
            
            # otherwise exist/DNE or <= 0 , simply decrement count
            mapper[ord(s[right])- ord('A')] -= 1

            # move pointer next
            right += 1

            # only occurs if our current window has full count
            while count == 0:
                # this is the check of res
                if right - left < minLength:
                    minLength = right - left 
                    # remember we checked first, then incremented right
                    res = s[left:right]
                # 
                if mapper[ord(s[left])- ord('A')] == 0:
                    count += 1
                mapper[ord(s[left])- ord('A')] += 1
                left += 1
        return res

    def minWindow(self, s:str, t:str) -> str:
        '''
        Sliding Window Hashmap
        RT : O(n)
        Space: O(n)
        '''
        if not s or not t or len(t) > len(s):
            return ''

        countT = collections.Counter(t)
        window = collections.defaultdict(int)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            # process this char
            char = s[right]
            window[char] += 1

            # if have a match
            if char in countT and window[char] == countT[char]:
                have += 1
            
            # if our current window is potential, contract
            while have == need:

                # update result potential
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)

                # start shrinking window
                window[s[left]] -= 1
                # if we removed a potential, decrement
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        left, right = res
        return s[left:right+1] if resLen != float('inf') else ''
            





    


        

            
            






        

            
            



