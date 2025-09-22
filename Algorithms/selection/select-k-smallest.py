
import heapq

def selectKthSmallest(arr, k):
    # Sorting and return
    # RT : O(nlogn)
    # Space: O(n) for extra array
    if not nums or k <= 0 or k >= len(arr): return []
    sorted_nums = sorted(nums)
    return sorted_nums[:k]


def selectKthSmallest(arr, k):
    # BUILT IN HEAPQ METHOD
    # RT: O(klogn)
    # Space: O(1)
    if not nums or k <= 0 or k >= len(arr): return []
    return heapq.nsmallest(k, nums) # (k, heap) where k is assume 0-indexed


def selectKthSmallest(arr, k):
    # Min Heap, Heapify, pop k smallest 
    # RT: O(nlogn)
    # space: O(1)
    if not arr or k >= len(arr): return None
    heapq.heapify(arr)
    res = []
    for i in range(k):
        res.append(heapq.heappop(arr))
    return res

def selectKthSmallest(arr, k):
    # MaxHeap, with k-space
    # Runtime: O(nlogk)
    # Space: O(k)
    if not arr or k >= len(arr): return None 
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