# stack last in first out
# push-add an element to the  top of stack
# pop-remove an element from the top of stack
# peek/top: retrieve the top element from the stack without removing it
# is_empty/check if the stack is empty

# queue first in first out
# enqueue-add an element to the end of the queue
# dequeue-remove an element from the front of the queue
# peek/front: retrieve the front element from the queue without removing it
# is_empty/check if the queue is empty

from collections import deque
 
queue = deque()

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

#dequeue
print(queue.popleft())  # 1
print(queue)  # deque([2, 3])

# peek/front
print(queue[0])  # 2
print(queue)  # deque([2, 3])

# is_empty/check if the queue is empty
is_empty=len(queue)==0
print(is_empty)  # False
print(queue)