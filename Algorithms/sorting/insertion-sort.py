
# Shifting LHS
def insertion_sort(arr: list[int]):

    # exceptions : empty array
    if not arr: return arr

    # iterate [1, n-1]
    for i in range(1, len(arr)):
        # grab this iteration value and shift ptr
        key = arr[i]
        j = i - 1
        # got ahead and compare and swap if needed
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        # at j < key, we know j+1 has been duped, replace
        arr[j+1] = key
    
    print(arr)




if __name__ == '__main__':
    insertion_sort([3,5,1,3,1,9])