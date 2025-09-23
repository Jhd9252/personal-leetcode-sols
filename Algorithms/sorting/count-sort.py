import collections
def count_sort(arr):
    # adjust for negatives, (-1, 5), then we need abs(min-max) + 1 
    # if both are positive, then mini goes at index 0 (1,5), have 5 spaces max(place)
    # occurence count
    # get the cum sum 
    # take the count, make it 0-index, place
    if not arr: return []
    mini = min(arr)
    maxi = max(arr)
    length = maxi - mini + 1

    occur = [0] * length
    res = [0] * len(arr)
    
    for num in arr:
        occur[num-mini] += 1

    for i in range(1, length):
        occur[i] += occur[i-1]

    

    for num in reversed(arr):
        idx = occur[num-mini] - 1 # the number is contrained by the mini -> minus 1 to switch to 0-index
        res[idx] = num 
        occur[num-mini] -= 1
    
    return res 


if __name__ == '__main__':
    arr = [4,3,6,3,5,8]
    res = count_sort(arr)
    print(res)



