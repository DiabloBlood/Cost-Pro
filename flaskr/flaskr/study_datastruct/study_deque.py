from collections import deque

queue = deque([1, 2, 3, 4, 5, 6])

# pop() is pop right
# print queue.pop()
queue.popleft()
print queue


# append is append right
# queue.append(7)
queue.appendleft(7)
print queue