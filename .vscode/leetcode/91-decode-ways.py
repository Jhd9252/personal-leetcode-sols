class Solution:
    def numDecodings(self, s: str) -> int:
        ''' 
        DP Bottom Up Tabulation:
        NOTE: Variation of nth staircase with [1,2] steps each.
        NOTE: Caution when handling edges cases and conditions.
        Realize that the ith index can be reached by 
        (1) taking 1 step from i - 1
        (2) taking 2 steps from i - 2
        Let dp[i] be the number of ways to parse s[1:i+1]

        '''
        if not s or s[0] == '0': return 0
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1 # base case
        for i in range(2, len(s) + 1):
            # add one step (if prev is valid)
            if 0 < int(s[i-1:i]):
                dp[i] += dp[i-1]
            # add two step if 
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        # Edge case check
        if s is None or s[0] == '0':
            return 0

        dp = [1] * len(s)

        for i in range(1, len(s)): 
            # One digit check
            dp[i] = 0 if int(s[i]) == 0 else dp[i - 1]

            # Two digit check
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i - 2 if i > 1 else 0]   
                
        # Return the last element
        return dp[-1]
            
        

        
        
                

    