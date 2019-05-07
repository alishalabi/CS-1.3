#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


# 86 <-> 01010110

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    total = 0
    power = len(digits) - 1
    # Decode digits from binary (base 2)
    if base == 2:
        # cycle through every digit in digits
        for digit in digits:
            digit = int(digit)
            # if digit == "1":
            # assign base power that will be added to total
            # print(digits.index(digit))
            # break
            total += digit * (2 ** power)
            power -= 1
        return total

    # Decode digits from hexadecimal (base 16)
    # ...
    if base == 16:
        for digit in digits:
            # convert digits to integers
            if digit.isdigit() == True:
                digit = int(digit)
                # add digit to total
                total += digit * (16 ** power)
                power -= 1
            else:
                digit = digit.lower()
                digit = string.hexdigits.index(digit)
                total += digit * (16 ** power)
                power -= 1

        return total

    # TODO: Decode digits from any base (2 up to 36)
    # ...
    else:
        max_string = "0123456789abcdefghijklmnopqrstuvwxyz"
        # Trim down the max string based on "bases" parameter
        new_string = max_string[:base]
        # print("New String:")
        # print(new_string)
        # Iterate through each digit
        for digit in digits:
            # Case: item is digit
            if digit.isdigit() == True:
                digit = int(digit)
                total += digit * (base ** power)
            else:
                digit = digit.lower()
                digit = new_string.index(digit)
                total += digit * (base ** power)
            power -= 1
        return total


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # Declare max string up to base 36
    max_string = "0123456789abcdefghijklmnopqrstuvwxyz"
    # TODO: Encode number in binary (base 2)
    # generare exponents until no exponent value is larger than number
    max_power = 0
    while base ** max_power <= number:
        max_power += 1
    max_base_token = base ** max_power
    """
    Sample input/output for 87:
    Max power: 6
    Max base token: 2^6 = 64
    """
    output = ""
    # As long as there is a value to remove, remove from number
    while number != 0:
        # Section inspired by nsafai
        remainder = number % base
        output += max_string[remainder]
        number = number // base

    return output[::-1]
    # End inspired section

    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    decoded_input = decode(digits, base1)
    encoded_output = encode(decoded_input, base2)
    return encoded_output


# def main():
#     """Read command-line arguments and convert given digits between bases."""
#     import sys
#     args = sys.argv[1:]  # Ignore script file name
#     if len(args) == 3:
#         digits = args[0]
#         base1 = int(args[1])
#         base2 = int(args[2])
#         # Convert given digits between bases
#         result = convert(digits, base1, base2)
#         print('{} in base {} is {} in base {}'.format(
#             digits, base1, result, base2))
#     else:
#         print('Usage: {} digits base1 base2'.format(sys.argv[0]))
#         print('Converts digits from base1 to base2')
#
#
# if __name__ == '__main__':
#     main()

decode("A0345", 15)
