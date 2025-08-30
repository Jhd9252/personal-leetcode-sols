import random
class Solution:
    '''
    M1. Sort, return nums[k-1] O(nlogn) with O(1) space
    M2. MinHeap with size k, O(nlogk) with O(k) Space
    M3. QuickSelect O(n**2) but really O(n) in place
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ''' Sorting '''
        nums.sort(reverse=True)
        return nums[k-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        ''' MinHeap with root being the kth largest '''
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        ''' Quickselect '''
        pass 