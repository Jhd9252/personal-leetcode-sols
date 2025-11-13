
# Find the matching substring
# linear time with O(len(substring))


def lps(substring):

    m = len(substring)
    lps = [0] * m 
    j = 0

    for i in range(1, m):
        while substring[i] != substring[j] and j > 0:
            # j <= 0, we start over anyways and lps is initialized to zero
            # otherwise, j > 0, and not match, we want to go into the spot where there was a prev match
            j = lps[j-1]
        if substring[i] == substring[j]:
            # if match, then move j upwards
            # we set lps[i] = j because we want to start match AFTER the prev prefix spot
            j += 1
            lps[i] = j
    return lps


def kmp(string, substring):
    n, m = len(string), len(substring)
    lps = lps(substring)
    res = []
    j = 0

    for i in range(n):
        # if there is no match, and j > 0, then we set j backwards to prev prefix match
        while string[i] != substring[j] and j > 0:
            j = lps[j-1]
        # if there is a match, we increment j for next char in substring to compare
        if string[i] == substring[j]:
            j += 1
            # however if j has reached the end, 
            if j == m:
                # we add the index of beginning of full match
                # which is current index - length of subtring - 1 (for zero index)
                res.append(i-m-1) # start point of full match 
                # since this ended on match, we set J to start at prev matching prefix again
                j = lps[j-1]
    return res