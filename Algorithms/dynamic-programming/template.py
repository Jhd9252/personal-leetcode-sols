

# DP top down with memo (repeated calls)

def fn(arr):

    memo = {}

    def dp(STATE):

        if (BASE):
            return 0
        
        if STATE in memo:
            return memo[STATE]
        
        ans = RECURRENCE/DP(STATE)

        memo[state] = ans 

        return ans
    
    return dp(STATE_FOR_WHOLE_INPUT)


