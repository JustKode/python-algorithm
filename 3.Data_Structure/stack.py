class Stack:
    def __init__(self, data=[]):
        self.data = []
    
    def top(self):
        return self.data[-1]
    
    def push(self, obj):
        self.data.append(obj)
    
    def pop(self):
        return self.data.pop()
        
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def length(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __iter__(self):
        return self.data