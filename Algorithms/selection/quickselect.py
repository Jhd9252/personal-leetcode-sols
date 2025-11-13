import numpy as np
import random

def quickselect(arr, k):
    if not arr or k <= 0 or k > len(arr): return []
    return sorted(arr)[k-1]

# np.partition -> assumes k is 1-indexed, must convert to 0-indexed
def quickselect(arr, key):
    if not arr or k <= 0 or k > len(arr): return []
    arr = np.array(arr)
    # creates array where left until k-1 is partitioned, with k-1 being last correct
    # return the only correct placement of index k-1
    return np.partition(arr, k-1)[k-1]

def quickselect(arr, key):
    if not arr or k <= 0 or k > len(arr): return None

    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return quickselect(left, key) if left else -1
    elif k < len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, key - len(left - len(mid))) if right else -1


# Examples:
if __name__ == "__main__":
    nums = [7, 2, 5, 3, 9, 1]
    k = 3
    print(quickselect(nums, k))  #[1,2,3,5,7,9], k = 3, index = 2, res = 3
