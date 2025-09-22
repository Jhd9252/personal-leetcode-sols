class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ''' Brute force find occurence j per i
        RT: O(n**2)'''
        pass
    def findSpecialInteger(self, arr: List[int]) -> int:
        ''' Brute Force Count and Sort'''

        freq = collections.Counter(arr)
        freq = [x[0] for x in sorted(freq.items(), key = lambda x:x[1], reverse = True)]
        return freq[0]

    def findSpecialInteger(self, arr: List[int]) -> int:
        '''
        Running HashMap
        RT: O(N)
        Space: O(n)
        '''
        threshold = len(arr) / 4
        freq = collections.defaultdict(int)
        for num in arr:
            freq[num] += 1
            if freq[num] > threshold:
                return num
    def findSpecialInteger(self, arr: List[int]) -> int:
        ''' 
        Running Counter
        Runtime: O(n)
        Space: O(1)
        '''
        count = 0
        prev = arr[0]
        threshold = len(arr) / 4
        for num in arr:
            if num == prev:
                count += 1
            else:
                count = 1
                prev = num 
            if count > threshold:
                return num 
    def findSpecialInteger(self, arr: List[int]) -> int:
        ''' 
        By sorting charactersitc and threshold, we check supposed int + threshold
        Runtime: O(n)
        space: O(1)
        '''
        threshold = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i+threshold]:
                return arr[i]
    
    
        

        
       
        