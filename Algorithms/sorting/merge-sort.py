def merge(A, B):
    left, right = 0, 0
    merged = []
    while left < len(A) and right < len(B):
        if A[left] < B[right]:
            merged.append(A[left])
            left += 1
        else:
            merged.append(B[right])
            right += 1
    merged += A[left:] or B[right:]
    return merged

def merge_sort(arr: list[int]) -> list[int]:
    # base case of zero length
    if len(arr) <= 1: return arr

    # recurse 
    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    return merge(left, right)

if __name__ == '__main__':
    res = merge_sort([5,4,6,3,2,6,66])
    print(res)
