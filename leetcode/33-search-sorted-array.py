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
    class Solution:
    def search(self, nums, target) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    
    def check (self, nums, left, mid, right, target):
        ''' Return True if target possibly in left side'''
        if nums[left] < nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                return True
        return False

    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # specific condition, not convergence, use <=
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid 

            # which side is sorted (we can only reliably judge the sorted side)
            # check if target is on that side
            # if left side is sorted, then we can check the range
            if nums[left] <= nums[mid]:
                # check if target in left (mid was already checked)
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # else target is not on left side, move left pointer past mid
                else:
                    left = mid + 1
            # if not left side sorted, then right
            # check if target is valid in this range
            else:
                # if it is, then move past mid (already checked mid)
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # else target not in this side, move right pointer before mid
                else:
                    right = mid - 1

        return -1 


                    



        
        
        