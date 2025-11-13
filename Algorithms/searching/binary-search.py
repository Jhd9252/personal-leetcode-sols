def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    # specific existence, want a final loop where left == right == last space
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 

<<<<<<< HEAD

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
=======
'''
Exact Match / Specific occurence / Existence   ->  left <= right, left = mid + 1, right = mid - 1

First occurence / left convergence ->               left < right, left = mid + 1, right = mid
We want only the left to have possible answer, right exclused

Last occurence / right convergence ->               left < right, left = mid, right = mid -1 
We want only the right to have a possible answer, left excluded. 
>>>>>>> 7aa4b632c2a2d184865571d548ec850dab15069a

'''
