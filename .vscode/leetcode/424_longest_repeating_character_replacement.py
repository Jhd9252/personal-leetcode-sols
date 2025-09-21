'''
424. Longest Repeating Character Replacement
Medium
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ''' 
        Brute Force: 
        1. Treat each index as the starting index of all its possible substrings
        2. We track each occurence and the most frequently occuring character
        3. The condition is the window - freqMost <= k. Otherwise break. 
        Runtime: O(n**2)
        Space: O(26) = O(1)
        '''
        res = 0
        for i in range(len(s)):
            tracker = collections.defaultdict(int) # {char:count}
            for j in range(i, len(s)):
                tracker[s[j]] += 1
                maxChar, maxFreq = max(tracker.items(), key = lambda x: x[1])
                if (j-i+1) - maxFreq > k:
                    break
                res = max(res, (j-i+1))
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window: 
        (1) Expand window on condition that window - maxFreq <= k
        (2) If condition holds, update result
        (3) Else condition false, move left ptr++ until condition is valid
        
        Runtime: O(n)
        Space: O(n)
        '''
        res = 0
        left = 0
        tracker = collections.defaultdict(int)
        for right in range(len(s)):
            tracker[s[right]] += 1
            maxChar, maxFreq = max(tracker.items(), key = lambda x: x[1])
            while (right - left + 1) - maxFreq > k:
                tracker[s[left]] -= 1
                left += 1
            res = max(res, (right - left + 1))
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window without maxFreq O(26) 
        Runtime: O(n)
        Space: O(n)
        '''
        res = 0
        left = 0
        tracker = collections.defaultdict(int)
        maxFreq = 0
        for right in range(len(s)):
            tracker[s[right]] += 1
            maxFreq = max(maxFreq, tracker[s[right]])
            while (right - left + 1) - maxFreq > k:
                tracker[s[left]] -= 1
                left += 1
            res = max(res, (right-left+1))
        return res 

    

                    
            




    
            

                
                
                
                
                
        
        