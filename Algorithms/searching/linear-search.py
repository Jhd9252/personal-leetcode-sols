
def linear_search(arr: list[int], target: int):
    for i, n in enumerate(arr):
        if n == target:
            return i
    return -1 