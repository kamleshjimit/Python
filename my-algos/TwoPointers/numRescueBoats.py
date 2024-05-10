def numRescueBoats(people: list[int], limit: int) -> int:
    """
    Boats to Save People
    You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time,
    provided the sum of the weight of those people is at most limit.
    >>> numRescueBoats([1,2], 3)
    1
    >>> numRescueBoats([3,2,2,1], 3)
    3
    >>> numRescueBoats([3,5,3,4], 5)
    4
    """   
    count = 0
    people.sort()
    left, right = 0, len(people) -1
    while left < right:
        if (people[left] + people[right] <= limit):
            left += 1
        right -= 1
        count += 1
        
    if left == right:
        count += 1
    return count
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
