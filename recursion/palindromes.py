#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """
    Complexity: O(n) where n is number of letters in text
    """
    # implement the is_palindrome function iteratively here
    # convert text to lower case
    text = text.lower()

    # Attempt 1
    # # iterate through all items in text
    # for index_left in range(len(text)):
    #     # declare second index variable
    #     index_right = (- index_left - 1)
    #     # ensure index_right/index_left are valid
    #     while text[index_right] not in string.ascii_lowercase:
    #         index_right -= 1
    #     while text[index_left] not in string.ascii_lowercase:
    #         index_left += 1
    #     # compare early index with (-i index - 1) - pair first w/ last, iterate
    #     if text[index_left] != text[index_right]:
    #         # find exit condition - pairs don't match
    #         return False
    # # iteration goes all the way through w/o breaking - successful palindrome
    # return True

    # Attempt 2 - Anisha's TA help
    index_left = 0
    index_right = len(text) - 1
    # Check to see if we have past the midpoint of text
    while index_left != index_right and index_left < index_right:

        # Correct / remove non chars
        if text[index_left] not in string.ascii_lowercase:
            index_left += 1
            continue

        # Correct / remove non chars
        if text[index_right] not in string.ascii_lowercase:
            index_right -= 1
            continue

        # Exit Scenario: left and right do not match, not palindrome
        if text[index_left] != text[index_right]:
            return False

        # Iterate both indexes
        index_left += 1
        index_right -= 1
    return True

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    """
    Complexity:
    """
    # implement the is_palindrome function recursively here
    text = text.lower()

    # Instantialize initial values for left and right (if none given)
    if left == None:
        left = 0
    if right == None:
        right = len(text) - 1

    # Exit condition - loop has been iterated through and has not broken
    if left == right or left > right:
        return True

    # Correct left index
    if text[left] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left + 1, right)

    # Correct right index
    if text[right] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left, right - 1)

    # Continue recursion
    if text[left] == text[right]:
        return is_palindrome_recursive(text, left + 1, right - 1)

    # Exit case: cannot add another recursive round, left and right are not equal
    return False

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
