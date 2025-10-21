import collections

# adjust count sort for negative values
# steps
# 1. occurence
# 2. cum sum 
# 3. placement

def count_sort(arr: list[int]):
    if not arr: return []
    mini = min(arr)
    maxi = max(arr)

    # mini and max are 1-index, convert to 0-index
    length = maxi - mini + 1

    occur = [0] * length    # index = val, val = occurence of index
    res = [0] * len(arr)

    # step 1. get occurences
    for num in arr: 
        occur[num - mini] += 1

    # step 2. cumulative sum -> placements in result
    for i in range(1, length):
        occur[i] += occur[i-1]

    # step 3. placement in result
    for num in reversed(arr):
        idx = occur[num-mini] - 1 # remember occurence is 1-indexed, move -1 for 0-index
        res[idx] = num
        occur[num-mini] -= 1
    
    return res 


if __name__ == '__main__':
    arr = [4,3,6,3,5,8]
    res = count_sort(arr)
    print(res)



