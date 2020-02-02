from collections import deque

class Queue:
    def __init__(self, data=[]):
        self.queue = deque(data)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def put(self, obj):
        self.queue.append(obj)
    
    def get(self):
        return self.queue.popleft()
        
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    
    def length(self):
        return len(self.queue)
    
    def __str__(self):
        return str(list(self.queue))
    
    def __len__(self):
        return len(self.queue)
    
    def __getitem__(self, index):
        return self.queue[index]
    
    def __iter__(self):
        return self.queue