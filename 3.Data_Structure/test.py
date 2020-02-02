from stack import Stack
from queue import Queue

# Stack
print("\n\nStack Start \n\n")
stack = Stack()
stack.push(1)
stack.push(2)
print(stack)
print(stack.top())
print(stack.is_empty())
print(stack.pop())
print(stack[0])
print(stack.length())
print(stack.pop())
print(stack.is_empty())
print(stack)

# Queue
print("\n\nQueue Start \n\n")
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
print(queue)
print(queue.front())
print(queue[0])
print(queue.rear())
print(queue.is_empty())
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.is_empty())