class Solution:
    '''
    We know that at the ith house, the max profit is either 
    (1) Not choosing this house -> dp[i-1]
    (2) Choosing this house -> nums[i] + dp[i-2]

    Since index (n-1) -> index (0), then we can only do either.
    Thus, we can apply the previous algorithm to two arrays. 
    '''
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        def solve(arr):
            n = len(arr)
            dp = [0] * n
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(arr[i] + dp[i-2], dp[i-1])
            return dp[-1]
        return max(solve(nums[1:]), solve(nums[:-1]))

    def rob(self, nums: List[int]) -> int:
        ''' save space '''
        def solve(nums):
            yes, no = 0, 0
            for num in nums:
                yes, no = num + no, max(yes, no)
            return max(yes, no)
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(solve(nums[1:]), solve(nums[:-1]))
        
        
        