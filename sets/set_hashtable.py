#!python
import sys
sys.path.append("../")
from hashtables.hashtable import HashTable


class Set(HashTable):
    def __init__(self, max_size):
        """
        initialize a new circular buffer that can store at most max_size items
        """
        HashTable.__init__(self)
        self.max_size = max_size

    # Inheriting contains from superclass
    # def contains(element):
    #     """
    #     return a boolean indicating whether element is in this set
    #     """
    #     return element is in self

    def add(self, element):
        """
        add element to this set, if not present already
        """
        if self.size < self.max_size:
            self.set(element)
        else:
            raise Exception('Set is full, could not add: {}'.format(element))

    def remove(self, element):
        """
        remove element from this set, if present, or else raise KeyError
        """
        self.delete(element)

    def union(self, other_set):
        """
        return a new set that is the union of this set and other_set
        Time-complexity: O(n) where n is number of elements in two sets
        """
        union_set = Set()
        # Append each element in first HT
        for element in self.keys():
            union_set.add(element)
        # Append each element in second HT (duplicates resolved in HT method)
        for element in other_set.keys():
            union_set.add(element)
        return union_set

    def intersection(self, other_set):
        """
        return a new set that is the intersection of this set and other_set
        """
        # Note: optimization worked out with Nicolai during class
        intersection_set = Set()

        # Find smaller set
        if self.size < other_set.size:
            smaller_set = self
            bigger_set = other_set
        else:
            smaller_set = other_set
            bigger_set = self

        # Loop through every item of smaller set to save time
        for element in smaller_set.keys():
            if bigger_set.contains(element):
                intersection_set.set(element)
        return intersection_set

    def difference(self, other_set):
        """
        return a new set that is the difference of this set and other_set
        """
        difference_set = Set()
        for element in self.keys():  # O(n)
            if element not in other_set.keys():  # O(1)
                difference_set.set(element)
        for element in other_set.keys():
            if element not in self.keys():
                difference_set.set(element)
        return difference_set

    def is_subset(self, other_set):
        """
        return a boolean indicating whether other_set is a subset of this set
        """
        if self.difference(other_set) is None:
            return True
        return False

    # *----------------------------------------------*
    # Begin Stretch Challenge Tests
    def is_empty(self):
        """
        check if the buffer is empty
        """
        pass

    def is_full(self):
        """
        check if the buffer is full
        """
        pass

    def enqueue(self, item):
        """
        insert item at the back of the buffer
        TODO: Time complexity
        """
        pass

    def dequeue(self):
        """
        remove and return the item at the front of the buffer
        TODO: Time complexity
        """
        pass
