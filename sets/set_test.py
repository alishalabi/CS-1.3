from set_hashtable import Set
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set(20)
        assert s.max_size == 20
        assert s.size == 0

    def test_contains(self):
        """
        return a boolean indicating whether element is in this set
        """
        s = Set(20)
        s.add('I')
        s.add('V')
        s.add('X')
        assert s.contains('I') == True
        assert s.contains('V') == True
        assert s.contains(0) == False
        assert s.contains(1) == False
        assert s.contains('X') == True

    def test_add(self):
        """
        add element to this set, if not present already
        """
        s = Set(3)
        assert s.keys() == []
        s.add('I')
        assert s.keys() == ['I']
        s.add('V')
        self.assertCountEqual(s.keys(), ['I', 'V'])  # Ignore item order
        s.add('X')
        self.assertCountEqual(s.keys(), ['I', 'V', 'X'])  # Ignore item order
        with self.assertRaises(Exception):
            s.add('A')  # Key does not exist

    def remove(self):
        """
        remove element from this set, if present, or else raise KeyError
        """
        s = Set(20)
        s.add('I')
        s.add('V')
        s.add('X')
        s.remove('I')
        assert self.assertCountEqual(s.keys(), ['V', 'X'])

    def union(self):
        """
        return a new set that is the union of this set and other_set
        """
        pass

    def intersection(self):
        """
        return a new set that is the intersection of this set and other_set
        """
        pass

    def difference(self):
        """
        return a new set that is the difference of this set and other_set
        """
        pass

    def is_subset(self):
        """
        return a boolean indicating whether other_set is a subset of this set
        """
        pass

    # *----------------------------------------------*
    # Begin Stretch Challenge Tests

    def test_is_empty(self):
        """
        check if the buffer is empty
        """
        pass

    def test_is_full(self):
        """
        check if the buffer is full
        """
        pass

    def test_enqueue(self):
        """
        insert item at the back of the buffer
        """
        pass

    def test_dequeue(self):
        """
        remove and return the item at the front of the buffer
        """
        pass
