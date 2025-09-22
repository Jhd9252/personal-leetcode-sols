import heapq

def selectKthLargest(arr, k):
    # SORT
    # runtime: O(nlogn)
    # space: O(1), inplace
    if not arr or k <= 0 or k >= len(arr): return []
    return sorted(arr)[:k]

def selectKthLargest(arr, k):
    # minHeap to have root be boundary of smallest in group
    # runtime: O(nlogn)
    # space: O(n)
    minHeap = [-x for x in arr]
    heapq.heapify(minHeap)
    res = []
    for _ in range(k):
        res.append(heapq.heappop(minHeap))
    return [-x for x in res]

def selectKthLargest(arr, k):
    # minHeap with k-space
    # runtime: O(nlogk)
    # space: O(k)
    minHeap = [x for x in arr[:k]]
    heapq.heapify(minHeap)
    for num in arr[k:]:
        print(minHeap)
        if num > minHeap[0]:
            heapq.heapreplace(minHeap, num)
    return minHeap


if __name__ == '__main__':
    nums = [7, 2, 5, 3, 9, 1]
    k = 3
    print(selectKthLargest(nums, k))  # Output: [5, 7, 9]
