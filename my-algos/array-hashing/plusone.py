def plusOne(digits: list[int]) -> list[int]:
    """
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.
    >>> plusOne([1,2,3])
    [1, 2, 4]
    >>> plusOne([4,3,2,1])
    [4, 3, 2, 2]
    """
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        
    return [1] + digits


if __name__ == "__main__":
    import doctest
    doctest.testmod()
