class Solution:
    '''
    Asking us to keep tracking of the top k closest. 
    Closest is defined as the least distance from (0,0)
    Thus, what we want is the minimum distance 
    a^2 + b^2 = c^2 
    sqrt((x-a)**2 + (y-b)**2)
    create a max heap
    Thus, for every point, we can determine the distance
    If the current dist less than [0], then replace
    '''

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ''' 
        Brute Force: Determine all distance and sort them 
        RT: O(nlogn)
        Space: O(n)
        '''
        for i in range(len(points)):
            x, y = points[i]
            dist = math.sqrt((x**2) + (y**2))
            points[i].append(dist)
        points.sort(key=lambda x:x[2])
        return [[x,y] for x,y,dist in points[:k]]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        MaxHeap in Python (minHeap)
        Runtime: O(nlogk)
        Space: O(n)
        '''
        maxHeap = []
        length = 0
        for x,y in points:
            dist = math.sqrt((x**2) + (y**2))
            if length < k:
                heapq.heappush(maxHeap, (-dist, x, y))
                length += 1
            elif dist < -maxHeap[0][0]:
                heapq.heapreplace(maxHeap, (-dist, x, y))
        return [[x, y] for dist, x, y in maxHeap]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Quicksort:
        Runtime: O(n**2) Worst cast, but theoretically O(n)
        Space: O(1)
        '''
        pass

    

        