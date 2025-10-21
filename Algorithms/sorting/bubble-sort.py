# comparison based carry
def bubble_sort(arr: list[int]):
    n = len(arr)

    for placement in range(n-1, -1, -1):
        for i in range(placement):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    print(arr)


if __name__ == '__main__':
    bubble_sort([4,5,9,33])

