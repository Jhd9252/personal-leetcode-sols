class Solution:

    def canJump(self, nums: List[int]) -> bool:
        ''' 
        DFS 
        If at each step, I can explore k possible jumps, and so on unti reach end
        O(n^(max(n))) TLE
        Space: O(n) stack recursion
        '''
        n = len(nums)
        # base case
        if len(nums) == 0:
            return False 
        if len(nums) == 1:
            return True
        def dfs(nums, n, i):
            # base case: out of bounds
            if i >= n:
                return False
            # in bounds, check if end
            if i == n - 1:
                return True
            
            # in bounds, not end, check zero
            if nums[i] == 0:
                return False

            # recurse on other possible indexes from here
            for j in range(1, nums[i] + 1):
                if dfs(nums, n, i+j):
                    return True
            return False
        return dfs(nums, n, 0)

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set()
        if len(nums) == 0: return False
        if len(nums) == 1: return True

        def dfs(nums, n, i):
            if i >= n: return False
            if i == n - 1: return True
            if nums[i] == 0: return False 

            visited.add(i)

            for j in range(1, nums[i] + 1):
                if i + j not in visited:
                    if dfs(nums, n, i + j):
                        return True
            return False 
        return dfs(nums, n, 0)

    def canJump(self, nums: List[int]) -> bool:
        '''
        Kadanes variant
        Each index can be reached, if the overall total reach possible > current index
        If we keep a cumulative sum of total possible reach, check each index
        For instance at index i, if current total reach is >= i, then possible
            So we update the total possible reach by max(curr, i + nums[i])
        If we reach the end, return True
        '''
        curr = 0
        # for every index
        for i in range(0, len(nums)):
            # check if this is reachable
            if curr < i: return False 

            # reachable -> update
            # max is either current, or new jump + current length
            curr = max(curr, nums[i] + i)

        # if we reach the end, then its possible
        return True

    def canJump(self, nums: List[int]) -> bool:
        '''
        DP with running sum (every step is a subproblem)
        Where each subproblem as overlaps with optimal solutions. 

        Consider each value as a dollar amount, where each step takes 1 dollar. 
        A sum of total steps to an optimal point == loss to take that in a single trip. 
        Taking 3 steps (3 dollars) to an index, is the same as taking a single (3 dollar) jump

        Optimal choice at each step is to replace our money whenever > current

        This ensures that we always have the most potential to jump and index is reachable. 
        '''
        # starting with zero dollars
        dollars = 0
        
        # for every step
        for num in nums:
            # if we went into debt, we can't continue
            if dollars < 0:
                return False 
            # if we found money > current, switch
            if dollars < num:
                dollars = num 
            # move to the next step
            dollars -= 1

        # if end, return True
        return True
            

    