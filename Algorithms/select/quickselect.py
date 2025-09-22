import numpy as np
import random

# np.partition (0-indexed)
def quickselect(arr, key):

    if not arr or k >= len(arr) or k <= 0: return None

    arr = np.array(arr)

    return np.partition(arr, k-1)[k-1]

# array partitioned
def quickselect(arr, key):

    if not arr or k >= len(arr) or k <= 0: return None

    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):

        return quickselect(left, key) if left else -1 
    
    elif k < len(left) + len(mid):

        return pivot
    
    else:

        return quickselect(right, k - len(left) - len(mid)) if right else -1 
    



# Examples:
if __name__ == "__main__":
    nums = [7, 2, 5, 3, 9, 1]
    k = 3
    print(quickselect(nums, k))  #[1,2,3,5,7,9], k = 3, index = 2, res = 3
