
import heapq

import heapq

def selectKSmallest(arr, k):
    # sorting and return
    # runtime: O(nlogn)
    # Space: O(n) extra array

    # exceptions
    if not arr or k <= 0 or k > len(arr): return []

    sorted_nums = sorted(nums)
    return sorted_nums[:k]

def selectKSmallest(arr, k):
    # built in heapq nsmallest method
    # runtime: O(nlogk)
    # space: O(1)
    if not arr or k <= 0 or k > len(arr): return []
    return heapq.nsmallest(k, nums) # (k, heap) where k is assume 0-indexed

def selectKSmallest(arr, k):
    # minheap
    # runtime: O(nlogn)
    # Space: O(1)

    if not arr or k > len(arr) or k <= 0: return []
    heapq.heapify(arr) # turns in minheap
    res = []
    for i in range(k):
        res.append(heapq.heappop(arr))
    return res 

def selectKSmallest(arr, k)
    # Max Heap as boundary
    # runtime: O(nlogk)
    # space: O(k)

    if not arr or k <= 0 or k > len(arr): return []
    maxHeap = [-num for num in arr[:k]]
    heapq.heapify(maxHeap)
    for num in arr[k:]:
        if num < -maxHeap[0]:
            heapq.heapreplace(maxHeap, -num)
    return [-x for x in maxHeap]

    

# Examples:
if __name__ == "__main__":
    nums = [7, 2, 5, 3, 9, 1]
    k = 3
    print(selectKthSmallest(nums, k))  # Output: [1, 2, 3]