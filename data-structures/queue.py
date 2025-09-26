class Queue:
    def __init__(self):
        self.q = []
    def is_empty(self):
        return len(self.q) == 0
    def enqueue(self, data):
        self.q.append(data)
    def dequeue(self):
        if self.is_empty(): 
            raise IndexError()
        return self.q.pop(0)

    def peek(self):
        if self.is_empty(): raise IndexError()
        return self.q[-1]
    def size(self):
        return len(self.q)