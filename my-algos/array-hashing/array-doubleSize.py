def getConcatenation(nums: list[int]) -> list[int]:
    """
    Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    Specifically, ans is the concatenation of two nums arrays.
    Return the array ans.

    >>> getConcatenation([1,2,1])
    [1, 2, 1, 1, 2, 1]
    >>> getConcatenation([1,3,2,1])
    [1, 3, 2, 1, 1, 3, 2, 1]
    """
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans


if __name__ == "__main__":
    import doctest
    doctest.testmod()
