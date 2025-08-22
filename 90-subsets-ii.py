class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, path, start):
            res.append(path) # local
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(nums, path + [nums[i]], i + 1)
        dfs(nums, [], 0)
        return res 

    def subsetsWithDup(self, nums):
        res = set()
        nums.sort()
        def dfs(nums, path):
            res.add(tuple(path)) # local 
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return list(res) 

    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for num in nums:
            res += [x + [num] for x in res]
        return list(set([tuple(x) for x in res]))
        
    