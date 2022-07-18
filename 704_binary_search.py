class Solution:
    def search(self, nums, target):
        # binary search in O(logn) time
        # given array of numbers in ascending order and target num
        # search target in nums.
        # if exists, return index
        # else return -1

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        idx = 0
        while l <= r:
            mid = (l+r) //2 
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1


nums = [-1,0,3,5,9,12]
target = 9
alpha = Solution()
bravo = alpha.search(nums, target)
print(bravo)