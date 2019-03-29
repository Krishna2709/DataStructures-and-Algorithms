"""Adding a couple methods to our LinkedList class,
    and use that to implement a Stack.
    > Stack class
    > Stack ops => push, pop
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Inserting a new element as the head of the LinkedList
    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    # Deleting the first (head) element in the LinkedList as return it
    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    # Push (add) a new element onto the top of the stack
    def push(self, new_element):
        return self.ll.insert_first(new_element)
        
    # Pop (remove) the first element off the top of the stack and return it
    def pop(self):
        return self.ll.delete_first()


''' 
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# Start setting up a Stack
stack = Stack(n1)

stack.push(n2)
stack.push(n3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(n4)
print stack.pop().value
'''