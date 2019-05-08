#!python


def contains(text, pattern):
    # O(n) complexity
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    # Edge cases: empty text or empty pattern
    if len(pattern) == 0:
        return True
    elif len(pattern) > len(text):
        return False

    # # Attempt 1:
    # # Setup a substring/substring index that is the length of the pattern
    # # Splice the first n items, where n is the length of pattern
    # current_index = len(pattern) - 1
    # sub_string = text[:(len(pattern) - 1)]
    #
    # # Set while control - current index is less than max index
    # while current_index <= (len(text) - 1):
    #    # If found, return true
    #     if sub_string == pattern:
    #         return True
    #     # If does not match pattern: shift substring to the right, check again
    #     else:
    #         current_index += 1
    #         sub_string[1:]
    #         sub_string += text[current_index]
    #
    # # Substring can no longer be shifted: pattern not found
    # return False

    # Attempt 2: working with Ikey
    # Iterate through every index in text
    for index in range(len(text)):
        # Compare whether or not first item in text matches first item in pattern
        if text[index] == pattern[0]:
            # Compare the length of the pattern after found index, see if same as pattern
            if text[index: index + len(pattern)] == pattern:
                # Exit case: pattern found
                return True
    return False


def find_index(text, pattern):
    # O(n) complexity
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)

    # Edge cases: empty text or empty pattern
    if len(pattern) == 0:
        return 0
    elif len(pattern) > len(text):
        return None

    # Iterate through every index in text
    for index in range(len(text)):
        # Compare whether or not first item in text matches first item in pattern
        if text[index] == pattern[0]:
            # Compare the length of the pattern after found index, see if same as pattern
            if text[index: index + len(pattern)] == pattern:
                # Exit case: pattern found
                return index
    return None


def find_all_indexes(text, pattern):
    # O(n) complexity
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    # Instantiate variable to store all indexes
    all_indexes = []

    # Edge cases: empty text or empty pattern
    if len(pattern) == 0:
        for index in range(len(text)):
            all_indexes.append(index)
        return all_indexes
    elif len(pattern) > len(text):
        return all_indexes

    # Iterate through every index in text (note: only iterating while pattern can still fit in text)
    for index in range(len(text) - len(pattern) + 1):
        # Compare whether or not first item in text matches first item in pattern
        if text[index] == pattern[0]:
            # Compare the length of the pattern after found index, see if same as pattern
            if text[index: index + len(pattern)] == pattern:
                # Exit case: pattern found
                all_indexes.append(index)
    return all_indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
