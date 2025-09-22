'''
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.


'''
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ''' 
        DP tabulation: Iterative set building 

        Intuition: Every new element can be used as a endpoint of previous subsets

        Intuition: For every element, we have a choice to include it in set (add to 
        all existing subsets) or to exclude it (do nothing to subsets). 

        For instance:
        [1,2,3] has: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
        '''
        ps = [[]]
        for num in nums: 
            ps += [x + [num] for x in ps]
        return ps

    ########################################################
    def dfs(self, nums, idx, stack, res):
        if idx >= len(nums):
            res.append(stack.copy())
            return

        stack.append(nums[idx])
        self.dfs(nums, idx + 1, stack, res)

        stack.pop()
        self.dfs(nums, idx + 1, stack, res)

    def subsets(self, nums):
        res = []
        stack = []
        self.dfs(nums, 0, stack, res)
        return res

    ########################################################
    def subsets(self, nums):
        '''
        If we have len(nums) = n, then there are 2^n possible subsets. 
        Thus, (1<<n) means 2^n.
        Then for i in range(1<<n) means from [0, 2^n-1].
        J iterates for each number in nums
        if i & (1<<j): means if the the ith bit == 1, and 2^j == 1
        Then we add nums[j] to the temporary subset
        After J finishes iterating over nums, we add that subset to result. 
        '''
        res = []
        nums.sort()
        # for each unique subset numbered [0, 2^n-1]
        for i in range(1<<len(nums)):
            tmp = []
            # we check if each number in that subset
            for j in range(len(nums)):
                # we do this by checking AND
                # this is a YES/NO operation
                # since all other bits are zero-default
                # it only checks isolated j-bit
                if i & 1 << j:
                    tmp.append(nums[j])
            # at the end of this set, add all included numbers
            res.append(tmp)
        return res



        