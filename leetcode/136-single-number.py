class Solution:
    '''
    Given non-emtpy arr of nums. 
    Know that every element appears twice, but one. 
    Return that single element. 
    Require; rt O(N), space O(1) 

    M1. Brute Force: Linear search with skip
        [A, A, B, C], then starting at index 0, compare next, skip + 2, repeat, break and return idx
        RT: O(nlogn) for sorting
        Space: O(1)
    M2. hashmap: linear iteration to find only 1 occurence. 
        RT: O(n)
        Spce: O(n)
    M3. Bit manipulation: XOR
        - XOR is communitive meaning A^B = B^A
        - XOR is associatetive meaning A^B^C = C^A^B
        - XOR is identiive meaning A^0 = A
        Thus, no matter how the array is arranged, [A, B, C, D, A, B, C, D, Z]
        We have that the characterstic that numbers either appear twice or once, helps
        All even occuring numbers cancel to 0. And we know that a single number XOR 0 = num
        As the bits flip, first occurences add, second occurences subtract, leaving only answer. 

    '''
    def singleNumber(self, nums) -> int:
        ''' Brute Force with sorting '''
        nums.sort()
        for i in range(0, len(n) - 2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

    def singleNumber(self, nums) -> int:
        seen = collections.defaultdict(int)
        for num in nums:
            seen[num] += 1
        for key in seen:
            if seen[key] == 1:
                return key

    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums: 
            xor ^= num
        return xor
        