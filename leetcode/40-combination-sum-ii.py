class Solution:
    '''
    Backtracking
    - unique combinations only, solution set cannot contain duplicaets
    - each number can only be used once
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target: return []
        res = []
        candidates.sort()
        def dfs(path, total, start):
            if total > target: return 
            if total == target:
                res.append(path)
                return 

            for i in range(start, len(candidates)):
                # If the prev integer was included, and same as currrent, duplicate seq
                # whenever we include something, its start == i
                # if we do not include or popped off, then go back to prev start, i + 1, difference
                # ith index ranges over what to include, if start == i, include, if i > start, exclude 
                # thus, if we exclude an element, then if sorted order, and prev == ith index, skip also
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break 
                dfs(path + [candidates[i]], total + candidates[i], i + 1)
        dfs([], 0, 0)
        return list(res)

        