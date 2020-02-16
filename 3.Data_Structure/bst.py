class Node:
    def __init__(self, obj):
        self.obj = obj
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, obj):
        self.root = self._insert(self.root, obj)
            
    def _insert(self, node, obj):
        if node is None:
            node = Node(obj)
        else:
            if obj <= node.obj:
                node.left = self._insert(node.left, obj)
            else:
                node.right = self._insert(node.right, obj)
        
        return node
    
    def delete(self, obj):
        self.root, deleted = self._delete(self.root, obj)
        return deleted
    
    def _delete(self, node, obj):
        if node is None:
            return node, False
        
        deleted = False
        if obj == node.obj:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif obj < node.obj:
            node.left, deleted = self._delete(node.left, obj)
        else:
            node.right, deleted = self._delete(node.right, obj)
        return node, deleted
    
    def get(self, obj):
        return self._get(self.root, obj)
        
    def _get(self, node, obj):
        if node is None:
            return None
        elif node.obj == obj:
            return node.obj
        elif node.obj > obj:
            return self._get(node.left, obj)
        else:
            return self._get(node.right, obj)
        
    def pre_order_execute(self, func):
        def _pre_order(node, func):
            if node is None:
                pass
            else:
                func(node.obj, func)
                _pre_order(node.left, func)
                _pre_order(node.right, func)
        _pre_order(self.root, func)
        
    def in_order_execute(self, func):
        def _in_order(node, func):
            if node is None:
                pass
            else:
                _in_order(node.left, func)
                func(node.obj)
                _in_order(node.right, func)
        _in_order(self.root, func)
        
    def post_order_execute(self, func):
        def _post_order(node, func):
            if node is None:
                pass
            else:
                _post_order(node.left, func)
                _post_order(node.right, func)
                func(node.obj)
        _post_order(self.root, func)
        