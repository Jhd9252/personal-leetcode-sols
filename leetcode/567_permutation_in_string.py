"""
567. Permutation in String (Medium)
https://leetcode.com/problems/permutation-in-string/


Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Brute Force: 
        (1) Iterate through every index, creating a truth array. 
        (2) Treat each index as a starting point for possible permutation
        (3) If not permuation, go to next
        (4) Compare O(26) hashmap == 0
        Runtime: O(n*m)
        Space: O(26*m)
        '''
        for i in range(len(s2)):
            count_s1 = collections.Counter(s1)
            for j in range(i, len(s2)):
                if s2[j] not in count_s1 or count_s1[s2[j]] <= 0:
                    break
                count_s1[s2[j]] -= 1
            if all(x[1] == 0 for x in count_s1.items()):
                return True
        return False

                 

    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Fixed Sliding Window
        (1) We know that a permutation of s1 has a window of size n
        (2) Thus, starting with this window, we increment this fixed window
        (3) We check if each window matches a permutation
        Runtime: O(n*m)
        Space: O(26*n)
        '''
        truth = collections.Counter(s1)
        window = len(s1)
        for i in range(len(s2) - window + 1):
            if collections.Counter(s2[i:i+window]) == truth:
                return True
        return False
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Fixed Sliding Window 
        (1) Optimize by only beginning if ith starting point is valid
        Runtime: O(m*n)
        Space: O(26)
        '''
        truth = collections.Counter(s1) #O(n)
        window = len(s1)
        for i in range(len(s2) - window + 1): 
            if s2[i] not in truth or s2[i+window-1] not in truth:
                continue
            if collections.Counter(s2[i:i+window]) == truth: 
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Fixed Sliding Window with Constant Comparison
        Runtime: O(n)
        Space: O(26) = O(1)
        '''
        # exceptions
        if len(s1) > len(s2):
            return False
        # get our truth and current window counts
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # truth
            s2Count[ord(s2[i]) - ord('a')] += 1 # curr window

        # get our constant comparison variable
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # iterate over s2 in fixed window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # increment the right pointer
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            # decrement our left pointer
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            # right moves in for loop, increment left pointer
            l += 1
        # loop ends before checking last match
        return matches == 26


s1 = 'ab'
s2 = 'eidbaooo'
alpha = Solution()
bravo = alpha.checkInclusion(s1,s2)
print(bravo)