''' 
    Making a Queue class using a list
'''

class Queue:
    def __init__(self,head=None):
        self.storage = [head]
    
    # Adding a new element to the queue...
    def enqueue(self, new_element):
        return self.storage.append(new_element)
    
    # First element in the queue...
    def peek(self):
        return self.storage[0]
    
    # Deleting the first element in the queue...
    def dequeue(self):
        return self.storage.pop(0)
    
'''
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()
'''