#!python
import sys
sys.path.append("../")
from linkedlists.linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.list.length()

    def enqueue(self, item):
        """
        Complexity: O(1) in all cases
        """
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.list.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """
        Complexity: O(1) in all cases
        """
        # Remove and return front item, if any
        if self.list.is_empty():
            raise ValueError('Queue is empty, cannot dequeue')
        else:
            old_head = self.list.head.data
            self.list.delete(old_head)
            return old_head


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return len(self.list)

    def enqueue(self, item):
        #  Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty() == True:
            return None
        else:
            return self.list[0]

    def dequeue(self):
        # Remove and return front item, if any
        if self.is_empty() == True:
            raise ValueError('Queue is empty, cannot dequeue')
        else:
            dequeued_item = self.list[0]
            del self.list[0]
            return dequeued_item


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
