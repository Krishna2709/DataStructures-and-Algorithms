# Lookup = = > ' https://docs.python.org/3/tutorial/datastructures.html ' < = =
# Queue implementation using collections package
from collections import deque

queue = deque(['Bill','Elon','Steve'])
queue.append('Warren')
queue.append('Brin')
queue.popleft()

