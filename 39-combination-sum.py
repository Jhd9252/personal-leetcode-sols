class Solution:
    '''
    Given an array of DISTINT candidates, and target integer
    Return a list of all UNIQUE combinations that add to integer.
    Same number can be chosen multiple times. 
    Is the input in sorted order?
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ''' This is inefficient '''
        res = set()
        def dfs(path):
            # base case where sum > target: return
            if sum(path) > target: return
            # base case where sum == target: add
            if sum(path) == target:
                res.add(tuple(sorted(path)))
            # other wise, for every level, for every num, dfs
            for num in candidates:
                path.append(num)
                dfs(path)
                path.pop()
        dfs([])
        return list(res)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, nums, target, path, res):
        if target < 0: return
        if target == 0:
            res.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], res)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(path, start, total):
            if total > target: return
            if total == target: res.append(path)
            for i in range(start, len(candidates)):
                dfs(path + [candidates[i]], i, total + candidates[i])
        dfs([], 0, 0)
        return res
        
    