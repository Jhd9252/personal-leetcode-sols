
# QUICKSORT : ARRAY
def quicksort(arr):
    if len(arr) <= 1: return []
    pval = arr[-1]
    left = quicksort([x for x in arr if x < pval])
    mid = quicksort([x for x in arr if x == pval])
    right = quicksort([x for x in arr if x > pval])
    return left + mid + right 

# QUICKSORT : PARTITION HELPER - INPLACE
def quicksort(arr, low, high):

    # helper -> random pivot, return idx 
    def partition(arr, low, high):
        
        # grab a random pivot 
        pivot = arr[low]

        # set our swap ptrs 
        i, j = low, high
        
        # as long as we increment/decr pointers, it will end 
        while True:

            # move left pointer until we find something to swap
            while arr[i] < pivot:
                i += 1

            # move right pointer until we find something to swap
            while arr[j] > pivot:
                j -= 1

            # if the pointers have crossed, then we know that j is the min guaranteed position in which placement 
            if i >= j:
                return j
            
            # otherwise, swap the two values at two pointers
            arr[i], arr[j] = arr[j], arr[i]
            
            # increment / decrement the two pointers 
            i += 1
            j -= 1
    
    # base case is if len == 0 or negative
    if low < high:

        # use helper
        pidx = partition(arr, low, high)

        # call sort on left and right of pivot index
        quicksort(arr, low, pidx)
        quicksort(arr, pidx+1, high)






if __name__ == '__main__':
    arr = [0,3,1,4,5,2,1,5,55,3,]
    quicksort(arr, 0, len(arr)-1)
    print(arr)


    
        

