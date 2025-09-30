
# easy way

pip install kmp-algorithm

from kpm install KPMMatcher
matcher = KPMMatcher(subtring)
index = matcher.search(string) # start index or -1 


# LPS - longest prefix suffix

def lps(substring):
    m = len(substring)
    lps = [0] * m
    left = 0
    for right in range(1, m):
        while substring[left] != substring[right] and j > 0:
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

