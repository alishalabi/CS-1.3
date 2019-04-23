from set_array import SetArray
import unittest


class SetArrayTest(unittest.TestCase):

    def test_init(self):
        # ht = HashTable(4)
        # assert len(ht.buckets) == 4
        # assert ht.length() == 0
        # assert ht.size == 0
        ...

    def test_contains():
        """
        return a boolean indicating whether element is in this set
        """
        ...

    def test_add():
        """
        add element to this set, if not present already
        """
        ...

    def remove():
        """
        remove element from this set, if present, or else raise KeyError
        """
        ...

    def union():
        """
        return a new set that is the union of this set and other_set
        """
        ...

    def intersection():
        """
        return a new set that is the intersection of this set and other_set
        """
        ...

    def difference():
        """
        return a new set that is the difference of this set and other_set
        """
        ...

    def is_subset():
        """
        return a boolean indicating whether other_set is a subset of this set
        """
        ...

    # *----------------------------------------------*
    # Begin Stretch Challenge Tests

    def test_is_empty():
        """
        check if the buffer is empty
        """
        ...

    def test_is_full():
        """
        check if the buffer is full
        """
        ...

    def test_enqueue():
        """
        insert item at the back of the buffer
        """
        ...

    def test_dequeue():
        """
        remove and return the item at the front of the buffer
        """
        ...
