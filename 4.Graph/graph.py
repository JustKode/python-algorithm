from collections import deque

class Graph:
    def __init__(self, dic):
        self.dict = dic
        
    
    def bfs(self, start, end):
        queue = deque([(start, [start])])
        
        while queue:
            n, path = queue.popleft()
            if n == end:
                return path
            else:
                for m in set(self.dict[n]) - set(path):
                    queue.append((m, path + [m]))
        
        return None
    
    
    def dfs(self, start, end):
        stack = [(start, [start])]
        result = []

        while stack:
            n, path = stack.pop()
            if n == end:
                result.append(path)
            else:
                for m in set(self.dict[n]) - set(path):
                    stack.append((m, path + [m]))
        
        if len(result) == 0:
            return None
        
        index, length = -1, len(self.dict) + 1
        
        for i in range(len(result)):
            if len(result[i]) < length:
                index = i
        
        return result[index]