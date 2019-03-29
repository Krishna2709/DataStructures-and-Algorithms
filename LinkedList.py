''' LinkedList in Python 
    Steps : 
    > Create a node
    > Create a LinkedList 
    > LinkedList - append, get_position, insert, delete, search
'''

# Creating a Root node...
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

# Creating a LinkedList - it contains the operations => append, get_position, insert, delete and search.
class LinkedList(object):
    def __init__(self,head):
        self.head = head
    
    # adding a new element into the chain...
    def append(self, new_element):
        current = self.head
        # Appending in the middle of the chain...
        if self.head:
            while current.next:
                current = current.next
                current.next = new_element
        # Appending at the root node...
        else:
            self.head = new_element
    
    # getting the element from a position
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            raise ValueError('Please enter a valid position')
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    # inserting an element at a position
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        # inserting at the root node
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        # inserting in the middle of the chain
        elif position > 1:
            while current and counter < position:
                if counter == position-1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
    
    # deleting an element from the list...
    def delete(self, value):
        current = self.head
        previous = None
        while current.value!= value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    # searching for an element in the chain...
    def search(self, value):
        current = self.head
        found = False
        while current and found is False:
            if current.next == value:
                found = True
            else:
                current = current.next
        # if the head reaches to the last position in the chain...
        if current is None:
            raise ValueError('List doesn\'t contain the element.')
        return current
