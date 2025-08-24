class Solution:
    '''
    Sliding Window:
        - Left goes to first 1 
        - Right = left, iterate, allowed 1 = key
        - get the max 
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        k = 0
        left = 0
        res = 0
        marked = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k += 1
                marked = right
            if k > 1:
                k -= 1
                left  = marked + 1
            res = max(res, right - left + 1 - k)

        return res - 1 if res == len(nums) else res

    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Dynamic Programming: 
        - Let dp[i][0] be the length of longest subarray of 1's, end at i.
        - Let dp[i][1] be length of longest subarray of 1's including one zero.
        - Traverse through nums and update dp
            - dp[0][0] = 1, if num[0] == 1, and 0 else
            - if nums[i] == 1, update dp[i][0] by looking at dp[i-1][0] + 1
            - do the same for dp[i][1]
            - if nums[i] == 0, then dp[i][0] = 0
            - then dp[i][1] = dp[i-1][0], because we added a zero. 
        '''
        n = len(nums)
        if sum(nums) == n: return n - 1
        
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = nums[0]
        
        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0], dp[i][1] = dp[i-1][0] + 1, dp[i-1][1] + 1
            else:
                dp[i][0], dp[i][1] = 0, dp[i-1][0]
        
        return max([i for j in dp for i in j])  