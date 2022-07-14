"""
Given 2 strings
Return true if second string contains a permutation of first string
Otherwise return false

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # method 1: sorting
        # each permutation will match if sorted
        # sort s1, use sliding window, sort window, check
        # 107 test cases passed, but time limit exceeded
        if s2 and not s1:
            return True
        s1 = ''.join(sorted(list(s1)))
        window = len(s1)
        for i in range(len(s2)):
            sub = s2[i:i+window]
            s3 = ''.join(sorted(list(sub)))
            if s1 in s3:
                return True
        return False


        # method 2: hashing / dictionary per subwindow
        from collections import Counter
        d1 = Counter(s1)
        window = len(s1)
        for i in range(len(s2)):
            sub = s2[i:i+window]
            d2 = Counter(sub)
            if d1 == d2:
                return True
        return False

        # method 3: rolling hashing / dictionary
        from collections import Counter
        d1 = Counter(s1)
        windowlength = len(s1)
        d2 = Counter(s2[:windowlength])
        if d1 == d2:
            return True
        for i in range(len(s2)-windowlength):
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
            if s2[i+windowlength] in d2:
                d2[s2[i+windowlength]] +=1
            else:
                d2[s2[i+windowlength]] = 1 
            if d1==d2:
                return True
        return False




s1 = 'ab'
s2 = 'eidbaooo'
alpha = Solution()
bravo = alpha.checkInclusion(s1,s2)
print(bravo)