#how to use collections.deque as FIFO queues:
from collections import deque
customQueue = deque(maxlen = 3)
print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
#when appended above the maxlen then the deque
#is similar to a circular queue that is being overriden
customQueue.append(4)
print(customQueue)
#append()=enqueue
#popleft()=dequeue ---> returns the element deleted
print(customQueue.popleft())
print(customQueue)