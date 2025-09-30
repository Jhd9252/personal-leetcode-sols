
# basic backtracking - every choice every step

def backtrack(choices, path, others):
    if (BASE_CASE):
        # do something / add to result
        return ans
    
    # otherwise, continue exploring conditional choices
    ans = 0
    for (ITERATE_OVER_INPUT):
        backtrack(choices, path + curr, others)
    return 


# basic backtracking - include exclude
def backtrack(choice, params):
    if (BASE_CASE):
        return # something
    
    # otherise, choose include
    params.append(option)
    backtrack(choice, params)
    params.pop()

    return params
    