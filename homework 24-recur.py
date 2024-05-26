# TASK 1
from typing import Optional, Union

def to_power(x: Union[int, float], exp: int) -> Optional[Union[int, float]]:
    """
    Returns x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.
    """
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    elif exp == 0:
        return 1
    elif exp == 1:
        return x
    else:
        return x * to_power(x, exp - 1)

# Test cases
print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))
# TASK 2
def is_palindrome(looking_str: str) -> bool:
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """
    if len(looking_str) <= 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])

# Test cases
print(is_palindrome('mom'))
print(is_palindrome('father'))
print(is_palindrome('o'))

# TASK 3
def mult(a: int, n: int) -> int:

    if n < 0:
        raise ValueError("This function works only with positive integers")
    return 0 if n == 0 else a + mult(a, n - 1)

# Test cases
print(mult(2, 4))
print(mult(2, 0))
print(mult(2, -3))
# TASK 4
def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """
    if len(input_str) <= 1:
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]

# Test cases
print(reverse("hello"))
print(reverse("o"))
# TASK 5
def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
    """
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    else:
        return int(digit_string[0]) + sum_of_digits(digit_string[1:])

# Test cases
print(sum_of_digits('26'))
print(sum_of_digits('1893'))
print(sum_of_digits('test'))
