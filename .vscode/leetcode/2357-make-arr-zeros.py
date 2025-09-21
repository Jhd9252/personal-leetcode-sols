class Solution:
    # given a non-negative int arry called nums
    # 1: choose pos int x, x <= smallest non-zero element in nums
    # 2: subtract x from every positive element in nums
    # return minimum number of operations to make every element equal to nums

    # [1,5,0,3,5] -> choose 1, ops 1, zeros 1
    # [0,4,0,2,4] -> choose 2, ops 2, zeros
    # [0,2,0,0,2] -> choose 2, ops 3
    # [0,0,0,0,0] -> done return 3 operations -> track all zeroes == length

    # (1) edge case [] -> return 0
    # (2) edge case [0,0,0] -> x must be positive, so less than or equal to, 0 operations
    # not floats? 
    
    def minimumOperations(self, nums: List[int]) -> int:
        # while loop -> break when number of zeros == n
        # O(n**2) runtime: at most, picking n-number of mins
        # space: O(1)

        if not nums: return 0
        n = len(nums)
        z = sum(1 for num in nums if num == 0)
        if z == n: return 0

        ops = 0
        while z < n:
            x = min(nums)
            for i in range(n):
                if nums[i] != 0:
                    nums[i] -= x
                    if nums[i] == 0:
                        z += 1
            ops += 1
        return ops

    def minimumOperations(self, nums: List[int]) -> int:
        # NOTE: each time, picking a min, we get rid of that number and duplicates
        # NOTE: this observation states that the number of ops == num of unique non-zeros
        # NOTE: each operation takes zeroes out at least 1 number + duplicates
        # NOTE: 0 <= num of uniques < n
        return len(set([x for x in nums if x >0]))






    
    

