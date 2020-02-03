import heapq

class Heap:
    def __init__(self, data=[], **kwarg):
        self.max = False
        
        if kwarg.get('max') is True:
            self.max = True
        
        if self.max:
            self.heap = list(map(lambda x: (-x, x), data))
        else:
            self.heap = list(map(lambda x: (x, x), data))
        heapq.heapify(self.heap)
        
    def push(self, obj):
        if self.max:
            heapq.heappush(self.heap, (-obj, obj))
        else:
            heapq.heappush(self.heap, (obj, obj))
    
    def pop(self):
        return heapq.heappop(self.heap)[1]
    
    def top(self):
        return self.heap[0][1]
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def __len__(self):
        return len(self.heap)
    
    def __iter__(self):
        return list(map(lambda x: x[1], self.heap))
    
    def __str__(self):
        return str(self.__iter__())
        