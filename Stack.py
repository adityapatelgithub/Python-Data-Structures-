"""This file contains class definition of Stack. Stack follows Last In First
Out (LIFO) implementation. ArrayStack uses Python List to implement stack.
LinkedListStack uses Linked Lists to implement stack"""


class ArrayStack:
    """Stack implementation using Python Lists. Initialize with no parameters"""

    def __init__(self):
        """Create empty stack."""
        self._data = []                 # nonpublic

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data)==0

    def push(self, element):
        """Add element to the top of stack"""
        self._data.append(element)

    def top(self):
        """Return the top element. If empty, raise Empty exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]           # array[-1] returns last element in the array

    def pop(self):
        """Remove and return the top element. If empty, raise Empty exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()         # array.pop()removes and returns the last element 
    
class LinkedListStack():
    """Stack implementation using Linked List. Initialize with no parameters"""
    class Node:
        def __init__(self, value, next):
            self._value = value
            self._next = next
    def __init__(self):
        """Create empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the sumer of elements in the Stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size==0

    def push(self, element):
        """Add element to the top of stack"""
        self._head = LinkedListStack.Node( element, self._head )
        self._size += 1 

    def top(self):
        """Return the top element"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._value

    def pop(self):
        """Remove and return the top element. If empty, raise Empty exception"""
        if self.is_empty():
            raise Empty('Stack is empty')
        result = self._head._value
        self._head = self._head._next
        self._size -= 1
        return result
    





        
    
