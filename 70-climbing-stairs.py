class Solution:
    '''
    Given a staircase that has n-steps
    Each time, we can take 1 or 2 steps
    How many distinct ways can we reach the top
    How many combinations of 1 or 2 can reach n
    the longest combination is all 1's, or n-steps
    the shortest combination is all 2's at (n//2) or (n//2) + 1 steps
    '''
    def climbStairs(self, n: int) -> int:
        ''' 
        M1: Brute force find all combinations using backtracking 
        Runtime: O(2^n)
        Space: O(2^n)
        '''
        res = [0]

        def backtrack(total):
            if total == n:
                res[0] += 1 # local
            if total > n:
                return
            for i in range(1,3):
                backtrack(total + i)
            
        backtrack(0)
        return res[0]

    def climbStairs(self, n: int) -> int:
        ''' M2. Fibonacci Series '''
        if n == 0 or n == 1: return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n: int) -> int:
        ''' 
        DFS Bottom up Tabulation 
        Intuition:
            - Starting from the bottom of the stairs. 
            - From any step, there are two ways to get there
            - (A) Taking one step from (i-1)th step
            - (B) Taking 2 steps from (i-2)th step
            - NOTE: Taking 1 + 1 step from (i-2) is covered in (A)

        Cases: 
            i = 0, ways = 1 
            i = 1, ways = 1
            i = 2, ways = 2
            i = 3, ways = 3
            i = 4, ways = 5
        NOTE: Except for unique case [0, 1], this holds true.
        '''
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return steps[-1]

    def climbStairs(self, n: int) -> int:
        '''
        Dynamic Programming: Bottom Up (Tabulation) -> Vars
        Intuition: Same as above, but using variables to save space
        RT: O(n)
        Space: O(1)
        '''
        prevprev, prev = 1, 1 # i = 0 = 1 AND i = 1 = 1
        for step in range(2, n+1):
            prevprev, prev = prev, prevprev + prev
        return prev
