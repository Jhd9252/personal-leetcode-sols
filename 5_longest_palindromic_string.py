class Solution:
    '''
    M1. Pick all possible start, pick all possible end, check palindrome O(n**3)
    M1. Per each index, start two expansions (even/odd) O(n**2)
    M2. DP O(n**2) runtime, O(n**2) sapce
    '''
    def m1_check(self, s, l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            
    def longestPalindrome(self, s: str) -> str:
        ''' 
        M1. Brute force, pick all possible start and end points, check
        runtime O(n**3)
        space: O(n)
        '''
        res = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.m1_check(s, i, j):
                    res = max(res, s[i:j+1], key = len)
        return res 
    
    def checkPalindrome(self, s, l, r):
        res = ''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res = s[l:r+1]
            l -= 1
            r += 1
        # breaks when mismatch
        return res

    def longestPalindrome(self, s: str) -> str:
        ''' 
        Method 2: Per index, start two expansions 
        runtime: O(n**2)
        space: O(n)
        '''
        res = ''
        for i in range(len(s)):
            even = self.checkPalindrome(s, i, i+1)
            odd = self.checkPalindrome(s, i, i)
            res = max([res, even, odd], key = lambda x: len(x))
        return res

    def longestPalindrome(self, s: str) -> str:
        ''' 
        DP 2d table 
        runtime: O(n**2)
        space: O(n**2)
        '''
        dp = [[False] * len(s) for i in range(len(s))]
        res = s[0]
        for i in range(len(s)):
            dp[i][i] = True 
        # ranging over columns (left right)
        for j in range(len(s)):
            # range over rows (thing japanese)
            for i in range(j):
                # its a match if CURRENT && (NEXT or INNER)
                if s[i] == s[j] and (dp[i+1][j-1] or j == i+1):
                    dp[i][j] = True
                    if j - i + 1 > len(res):
                        res = s[i:j+1]
        return res

