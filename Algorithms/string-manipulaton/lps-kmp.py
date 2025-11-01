
# easy way

!pip instal kmp-algorithm

from kmp import KPMMatcher
matcher = KMPMatcher(substring)
index = matcher.search(string) # start index or -1


# LPS - longest prefix suffix
def lps(substring):
    # compare substring indexes with last match within it
    m = len(substring)
    lps = [0] * m
    left = 0
    for right in range(1, m):
        while substring[left] != substring[right] and left > 0:
            left = lps[left - 1]
        if substring[left] == substring[right]:
            left += 1
            lps[right] = left

    return lps

def kpm(string, substring):
    m, n = len(string), len(substring)
    lps = lps(substring)
    res = []
    left = 0
    for right in range(n):
        while string[right] != substring[left] and left > 0:
            left = lps[left - 1]
        if substring[left] == string[right]:
            left += 1
            if left == n:
                res.append(right)
    return res if res else -1

