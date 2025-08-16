'''
33. Search in Rotated Sorted Array
Medium
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''
class Solution:
    def check (self, nums, left, mid, right, target):
        ''' Return True if target possibly in left side'''
        if nums[left] < nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                return True
        return False
        
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            # mid is taken out of the possibilites
            if nums[mid] == target:
                return mid

            # first check which side is sorted
            # then within each side, check if target is there

            # left side is sorted
            if nums[left] <= nums[mid]:
                # check if target on sorted left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # else target not within sorted range
                else:
                    left = mid + 1
            # the right side is sorted
            else:
                if nums[mid] <  target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 


                    



        
        
        