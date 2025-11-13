
# recursion 
def fib(n: int):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)


# dp top down memo optimization
def fib(n: int):
    memo = {}

    def dp(state):
        # base cases
        if state == 0: return 0
        if state == 1: return 1
        if state == 2: return 1

        # pre process (check memo)
        if state in memo:
            return memo[state]
        
        # process - recursion
        # post process - assignment
        memo[state] = dp(n-1) + dp(n-2)

        # return upwards
        return memo[state]
    
    return dp(n)


# dp bottom up tabulation 1dp
def fib(n: int):
    # base case
    # fib(0) = 0
    # fib(1) = 1
    # fib(2) = 1
    # fib(3) = 2
    # starting with fib(1), fib(2)
    prev, curr = 1, 1
    for i in range(3, n+1):
        tmp = prev + curr # fib(i)
        prev, curr = curr, tmp
    return curr






