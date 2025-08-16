'''
739. Daily Temperatures
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Brute force with two for loops
        Result array is initialized to zero to acount for increased temperature.
        '''
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break 
        return res 

    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] # (val, idx)
        res = [0] * len(temps)

        for idx, num in enumerate(temps):
            while stack and num > stack[-1][1]:
                past_idx, past_num = stack.pop()
                res[past_idx] = idx - past_idx 
            stack.append((idx, num))
        return res 

    