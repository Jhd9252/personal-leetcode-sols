def searchMatrix(matrix, target): # return boolean target in matrix
	# brute force method
	# 81 ms running time
	# 14.5 MB memory usage
	# O(n^2) running time
	for i in matrix:
		for j in matrix[i]:
			if matrix[i][j] == target:
				return True
	return False


	# using binary search
	# treating 2d matrix as 2d matrix, or a list of m*n length
	# running time O(logn)
	m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1
    while low <= high:
        mid = (low + high) // 2
        x = matrix[mid//n][mid%n]
        if x < target:
            low = mid + 1
        elif x > target:
            high = mid - 1
        else:
            return True
    return False

