class SetArray(object):
    def __init__(self, max_size):
        """
        initialize a new circular buffer that can store at most max_size items
        """
        self.size = 0
        self.max_size = max_size
        ...

    def contains(element):
        """
        return a boolean indicating whether element is in this set
        """
        return element is in self

    def add(element):
        """
        add element to this set, if not present already
        """
        if element not in self:
            self.append(element)
        ...

    def remove(element):
        """
        remove element from this set, if present, or else raise KeyError
        """
        if element in self:

        ...

    def union(other_set):
        """
        return a new set that is the union of this set and other_set
        """
        ...

    def intersection(other_set):
        """
        return a new set that is the intersection of this set and other_set
        """
        ...

    def difference(other_set):
        """
        return a new set that is the difference of this set and other_set
        """
        ...

    def is_subset(other_set):
        """
        return a boolean indicating whether other_set is a subset of this set
        """
        ...

    # *----------------------------------------------*
    # Begin Stretch Challenge Tests
    def is_empty():
        """
        check if the buffer is empty
        """
        ...

    def is_full():
        """
        check if the buffer is full
        """
        ...

    def enqueue(item):
        """
        insert item at the back of the buffer
        TODO: Time complexity
        """
        ...

    def dequeue():
        """
        remove and return the item at the front of the buffer
        TODO: Time complexity
        """
        ...
