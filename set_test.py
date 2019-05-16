# Note: Tests and Sets were collaborated on with https://github.com/nsafai/

from set_hashtable import Set
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0

    def test_size(self):
        s = Set()
        assert s.size == 0
        s.add('I')
        assert s.size == 1
        s.add('V')
        assert s.size == 2
        s.removes('V')
        assert s.size == 1

    def test_contains(self):
        """
        return a boolean indicating whether element is in this set
        """
        s = Set()
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
        s = Set()
        assert s.keys() == []
        s.add('I')
        assert s.keys() == ['I']
        s.add('V')
        self.assertCountEqual(s.keys(), ['I', 'V'])  # Ignore item order
        s.add('X')
        self.assertCountEqual(s.keys(), ['I', 'V', 'X'])  # Ignore item order
        # with self.assertRaises(Exception):
        #     s.add('A')  # Key does not exist

    def test_remove(self):
        """
        remove element from this set, if present, or else raise KeyError
        """
        s = Set()
        s.add('I')
        s.add('V')
        s.add('X')
        s.remove('I')
        assert ("I" not in s)

    def test_union(self):
        """
        return a new set that is the union of this set and other_set
        """
        s1 = Set()
        s1.add('I')
        s1.add('V')
        s1.add('A')
        s2 = Set()
        s2.add('I')
        s2.add('V')
        union_s = s1.union(s2)
        self.assertCountEqual(union_s.keys(), ['I', 'V', 'A'])
        s2.add('B')
        union_s = s1.union(s2)
        self.assertCountEqual(union_s.keys(), ['I', 'V', 'A', 'B'])

    def test_intersection(self):
        """
        return a new set that is the intersection of this set and other_set
        """
        s1 = Set()
        s1.add('I')
        s1.add('V')
        s1.add('B')
        s2 = Set()
        s2.add('I')
        s2.add('V')
        intersection_s = s1.intersection(s2)
        self.assertCountEqual(intersection_s.keys(), ['I', 'V'])
        s2.add('B')
        intersection_s = s1.union(s2)
        self.assertCountEqual(intersection_s.keys(), ['I', 'V', 'B'])

    def test_difference(self):
        """
        return a new set that is the difference of this set and other_set
        """
        s1 = Set()
        s1.add('I')
        s1.add('V')
        s1.add('A')
        s2 = Set()
        s2.add('I')
        s2.add('V')
        difference_s = s1.difference(s2)
        self.assertCountEqual(difference_s.keys(), [])
        s2.add('B')
        difference_s = s1.difference(s2)
        self.assertCountEqual(difference_s.keys(), ['B'])

    def test_is_subset(self):
        """
        return a boolean indicating whether other_set is a subset of this set
        """
        s1 = Set()
        s1.add('I')
        s1.add('V')
        s1.add('A')
        s2 = Set()
        s2.add('I')
        s2.add('V')
        assert s1.is_subset(s2) == False
        # assert s2.is_subset(s1) == True
        s2.add('B')
        assert s1.is_subset(s2) == False

    # *----------------------------------------------*
    # # Begin Stretch Challenge Tests
    #
    # def test_is_empty(self):
    #     """
    #     check if the buffer is empty
    #     """
    #     # s = Set(5)
    #     # assert self.is_empty() == True
    #     # s.add("A")
    #     # s.add("B")
    #     # assert self.is_empty() == False
    #     # s.remove("A")
    #     # assert self.is_empty() == False
    #     # s.remove("B")
    #     # assert self.is_empty() == True
    #     pass

    # def test_is_full(self):
    #     """
    #     check if the buffer is full
    #     """
    #     # s = Set(3)
    #     # assert self.test_is_full() == False
    #     # s.add("A")
    #     # assert self.test_is_full() == False
    #     # s.add("B")
    #     # assert self.test_is_full() == False
    #     # s.add("C")
    #     # assert self.test_is_full() == True
    #     # with self.assertRaises(Exception):
    #     #     s.add("Z")  # Try to add item when full (redundant)
    #     # s.remove("A")
    #     # assert self.test_is_full() == False
    #     # s.remove("B")
    #     # assert self.test_is_full() == False
    #     pass

    # def test_enqueue(self):
    #     """
    #     insert item at the back of the buffer
    #     """
    #     pass
    #
    # def test_dequeue(self):
    #     """
    #     remove and return the item at the front of the buffer
    #     """
    #     pass
