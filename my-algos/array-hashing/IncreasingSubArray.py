def longestMonotonicSubarray(nums: list[int]) -> int:
    """
    3105. Longest Strictly Increasing or Strictly Decreasing Subarray
    You are given an array of integers nums. Return the length of the longest 
    subarray of nums which is either 
    strictly increasing or strictly decreasing
.
    >>> longestMonotonicSubarray([1,4,3,3,2])
    2
    >>> longestMonotonicSubarray([3,3,3,3])
    1
    """
    if not nums:
        return 0
        
    increasing_length = 1
    decreasing_length = 1
    max_length = 1
        
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            increasing_length += 1
            decreasing_length = 1
        elif nums[i] < nums[i - 1]:
            decreasing_length += 1
            increasing_length = 1
        else:
            increasing_length = 1
            decreasing_length = 1
            
        max_length = max(max_length, increasing_length, decreasing_length)
        
    return max_length


if __name__ == "__main__":
    import doctest
    doctest.testmod()
