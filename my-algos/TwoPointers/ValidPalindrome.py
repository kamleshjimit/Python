def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.

    A palindrome is a phrase that reads the same forward and backward after converting
    all uppercase letters to lowercase and removing all non-alphanumeric characters.

    Args:
        s: The input string.

    Returns:
        True if the string is a palindrome, False otherwise.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True

    >>> is_palindrome("race a car")
    False

    >>> is_palindrome(" ")
    True

    >>> is_palindrome("race car")
    True

    >>> is_palindrome("hello")
    False
    """

    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while end > start and not s[end].isalnum():
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
