def containsDuplicate(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    
    >>> containsDuplicate([1,2,3,1])
    True
    >>> containsDuplicate([1,2,3,4])
    False
    >>> containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    True

    """
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False;        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
