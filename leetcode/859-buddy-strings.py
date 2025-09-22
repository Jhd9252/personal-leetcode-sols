class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # if different lengths -> False
        if len(A) != len(B): return False
        # if same lengths and same string, need two same for true
        if A == B and len(set(A)) < len(A): return True
        # else, get the differences == 2
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        # check there are only 2 diffs, check that diffs can be swapped
        return len(dif) == 2 and dif[0] == dif[1][::-1]