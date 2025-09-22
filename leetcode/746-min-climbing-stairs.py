class Solution:
    '''
    Given n-stairs
    Given cost array where cost[i] is the cost of ith step. 
    From there, we can climb one or two steps. 
    We can start from the 0th step, or 1st step. 
    return the minimum cost to reach the top floor
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        We could use backtracking to try every possible combination
        '''
        pass

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''' 
        Recursion 
        (1) overlapping subproblems check (2) optimal substructure check
        If we can only take 1 or 2 steps, then from (i-1) or (i-2).
        Thus the lowest cost to reach nth step, is the min(i-1, i-2) + current cose
        '''
        def dp(i):
            if i < 2:
                return cost[i]
            return cost[i] + min(dp(i-1), dp(i-2))
        
        return min(dp(len(cost) - 1), dp(len(cost)-2))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''' DP bottom up tabulation '''
        dp =[0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])



    

    