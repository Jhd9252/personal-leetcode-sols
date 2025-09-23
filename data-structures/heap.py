# min heap 
import heapq
minheap = []
heapq.heapush(minheap, 1)
heapq.heapush(minheap, 5)
heapq.heapush(minheap, 2)
heapq.heappop(minheap)

class MinHeap:
    def __init__(self, arr=None):
        self.arr = arr if arr else []
    
    def parent(self, i):
        return (idx - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 + i + 2
    
    def _sift_up(self, i):
        ''' After insertion as leaf '''
        parent = self.parent(i)
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.parent[i]

    def _sift_down(self, i):
        ''' After deletion where you replace with largest '''
        while True:
            smallest = i
            left = self.left(i)
            right = self.right(i)

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left 
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right 
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest 
    def insert(self, data):
        ''' Insert as leaf, then sift up'''
        self.heap.append(data)
        self._sift_up(len(self.stack) - 1)
     
    def delete_min(self, data):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        # grab for return
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

