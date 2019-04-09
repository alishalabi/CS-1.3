#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    if array[index] == item:
        return index
    elif index < (len(array) - 1):
        return linear_search_recursive(array, item, (index + 1))
    else:
        return None

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # Define initial array that will eventually be sliced
    chunk = array
    # Scenario: item not found, chunk can still be searched
    while len(chunk) > 0:
        half_mark_index = int(len(chunk) / 2)
        if array.index(item) == half_mark_index:
            return array.index(item)
        elif array.index(item) < half_mark_index:
            chunk = chunk[:half_mark_index]
        else:
            chunk = chunk[half_mark_index:]
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


# names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']

def binary_search_recursive(array, item, left=None, right=None):
    # implement binary search recursively here

    # Slice array based on left/right
    chunk = []
    if right is not None:
        chunk = array[:right]
    elif left is not None:
        chunk = array[left:]

    # Exit Scenario: array can no longer be searched, item not in array
    if len(chunk) == 0:
        return None
    half_mark_index = int(len(chunk) / 2)

    # Exit Scenario: item found
    if chunk.index(item) == half_mark_index:
        return array.index(item)

    # Recursion Scenario: item occurs in first half of array
    elif chunk.index(item) < half_mark_index:
        return binary_search_recursive(array, item, None, array.index(half_mark_index))

    # Recustion Scenario: item does not occur in first half of array
    else:
        # elif chunk.index(item) < half_mark_index:
        return binary_search_recursive(array, item, array.index(half_mark_index), None)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


# names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
# print(linear_search(names, "Brian"))
