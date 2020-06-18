"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
"""
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size = self.size + 1
        return value

    def pop(self):
        if self.size < 1:
            return None
        value = self.storage[-1]
        self.storage.pop(-1)
        self.size = self.size -1
        return value
"""

import singly_linked_list

LinkedList = singly_linked_list.LinkedList
Node = singly_linked_list.Node

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size = self.size + 1
        return value

    def pop(self):
        if self.size < 1:
            return None
        value = self.storage.head.value
        self.storage.remove_head()
        self.size = self.size -1
        return value