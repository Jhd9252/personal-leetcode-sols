class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Brute Force: For each window, get the max
        Runtime: O((n-k)*k)
        Space: O(n-k)
        '''
        res = []
        left = 0
        for right in range(k-1, len(nums)):
            res.append(max(nums[left:right+1]))
            left += 1
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ''' 
        Sliding Window 
        - as we slide, we track the current max
        - if the current max is off, we recalc
        '''
        pass
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Monotonic Increasing queue of length k
        - starting with a full k length queue, pop off everything but last.
        - starting appending new right, popping left
        - each left is appended to res
        '''
        pass 

    

        
    