class Solution:
    '''
    Given array of nums -> distinct integers
    Return ALL POSSIBLE permutations in any order. 
    1 <= NUMS.length <= 6

    M1. Backtracking (level copy of available integers left)
    (1) base case is when local copy of avail ints are length zero -> add to result
    (2) Recurse on all possible integers left
    (3) Permutation where order matters
    '''
    def permute(self, nums):
        '''
        M1. Backtracking (with global ref)
        Runtime: O(n*n!)
        Space: O(n!)
        '''
        def dfs(nums, perm=[], res=[]):
            if not nums: 
                # NOTE: append a copy because the recursion uses a single stack path
                res.append(perm[::]) 

            for i in range(len(nums)): # [1,2,3]
                newNums = nums[:i] + nums[i+1:]
                perm.append(nums[i]) # here is direct manipulation of reference
                dfs(newNums, perm, res) # - recursive call will make sure I reach the leaf
                perm.pop() # NOTE: Since working with single path var, pop() 
            return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        ''' 
        M1. Backtracking (level copy of avail integers left) 
        Runtime: T(n) = aT(n-b) + f(n), where a = 1, balanced, n*f(n) = n!*n = O(n*n!)
        Space: Stack space O(n), array space per level O(n), but result is O(n!)
        '''
        res = []
        def dfs(nums, path):
            # base case, where avail length == 0
            if not nums:
                # NOTE: appending local variable/ref
                res.append(path)
                return

            # otherwise, recurse on avail ints
            for i in range(len(nums)):

                # notice how we are using new local vars, allows direct append
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])

        dfs(nums, [])
        return res

    def permute(self, nums) -> list[list[int]]:
        ''' 
        M1. Backtracking (with DFS iterative)
        Runtime: O(n!*n)
        Space: O(n!)
        '''
        stack = [(nums, [])] # starting with full avail, no chosen yet
        res = []

        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                stack.append((nums[:i] + nums[i+1:], path + [nums[i]]))
        return res

    def permute(self, nums) -> list[list[int]]:
        '''
        M1. backtracking (bfs iterative queue)
        Runtime:
        Space:
        '''
        q = deque([(nums, [])])
        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                q.append((nums[:i] + nums[i+1:], path + [nums[i]]))
        return res


    
    