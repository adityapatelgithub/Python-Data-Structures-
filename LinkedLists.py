class LinkedList:
    """A simple singly linked list"""
    class Node:
        """A simple singly linked list node"""
        def __init__(self, v, n):
            self._value = v
            self._next = n
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __str__(self):
        array = []
        current = self._head
        while current is not None:
            array.append(str(current._value))
            current = current._next
        return ' '.join(array)
    def add_before_head(self,value):
        """Add a value at the front of the list"""
        self._head = LinkedList.Node( value, self._head )
        if self._tail is None:      # empty list
            self._tail = self._head
        self._size += 1 
    def remove_before_head(self):
        """Retrieve a value from front of the list
        Assumes the list is not empty"""
        result = self._head._value
        self._head = self._head._next
        if self._head is None:      # now empty list
            self._tail = None
        self._size -= 1
        return result
    def add_after_tail(self, value):
        newNode = LinkedList.Node(value, None)
        if self._tail is None:
            self._head = self._tail = newNode
        else:
            self._tail._next = newNode
            self._tail = self._tail._next
        self._size += 1
    def top(self):
        return self._head._value
    def is_empty(self):
        return self._head is None
    def __len__(self):
        return self._size


        
        
