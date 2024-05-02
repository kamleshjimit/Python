def isValid(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    >>> isValid("()")
    True
    >>> isValid("()[]{}")
    True
    >>> isValid("(]")
    False
    """
    stack = []  # Stack to keep track of opening brackets
    mapping = {")": "(", "}": "{", "]": "["}  # Mapping for closing brackets

    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack.pop() != mapping[char]:  # Mismatched closing bracket
                return False
        else:  # Opening bracket
            stack.append(char)
    return not stack

if __name__ == "__main__":
    import doctest
    doctest.testmod()
