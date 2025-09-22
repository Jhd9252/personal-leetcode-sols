class Solution:
    '''
    Find recursive relation
    Recursive (top-down)
    Recursive + memo (top-down)
    Iterative + memo (bottom-up)
    Iterative + N variables (bottom-up)


    Cannot rob adjacent houses
    we know that the number of houses could be 1 <= 100 inclusie
    we know that the money at each house could be 0<=400 inclusive, 

    m1. backtracking while skipping the next house 

    m2. dp bottom up
    we know that each house has $[0, 400] -> makes it easier since we can always add
    At each step, the most profitable choice, is between
    max: (1) this house and n-2 (2) not this house, and n-1

    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
    
        

        