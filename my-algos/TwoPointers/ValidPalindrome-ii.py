def is_palindrome(s: str) -> bool:
    """
    Checks if a given string can be a palindrome after deleting at most one character.

    Args:
        s: The input string.

    Returns:
        True if the string can be a palindrome after deleting at most one character,
        False otherwise.

    >>> is_palindrome("aba")
    True

    >>> is_palindrome("abca")
    True

    >>> is_palindrome("abc")
    False

    >>> is_palindrome("a")
    True

    >>> is_palindrome("race")
    False
    """

    start = 0
    end = len(s) - 1
    skips = 0

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        elif skips < 1 and s[start + 1] == s[end]:
            start += 1
            skips += 1
        elif skips < 1 and s[start] == s[end - 1]:
            end -= 1
            skips += 1
        # elif start + 1 < end-1 and skips < 1 and s[start+1] == s[end-1]:
        #     skips += 1
        else:
            return False

    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
