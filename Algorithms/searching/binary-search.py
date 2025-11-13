def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    # specific existence so we want one final loop where left == right for a check
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 


'''
Exact match:       
    left <= right
    left = mid + 1
    right = mid - 1

odd + even = odd, mid is always left 
check mid, if not , left = mid + 1 first possible occur

First Occurence:    
    left <  right
    left = mid + 1
    right = mid 

# odd + even = odd, mid is always left
check mif, if not, left = mid, then its always on right

Last Occurence:     
    left <  right
    left = mid   
    right - mid - 1

'''
