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

'''
Exact Match / Specific occurence / Existence   ->  left <= right, left = mid + 1, right = mid - 1

First occurence / left convergence ->               left < right, left = mid + 1, right = mid
We want only the left to have possible answer, right exclused

Last occurence / right convergence ->               left < right, left = mid, right = mid -1 
We want only the right to have a possible answer, left excluded. 

'''
