# Shifting on card at a time into LHS

def insertion_sort(arr: list[int]):

    # exceptions
    if not arr: return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key


    print(arr)
        




if __name__ == '__main__':
    insertion_sort([3,5,1,3,1,9])