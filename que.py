from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
print(queue.popleft())  # 10

# Peek
print(queue[0])         # 20
