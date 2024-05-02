
import random

def findKthLargest(nums: list[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Can you solve it without sorting?

    >>> findKthLargest([3,2,1,5,6,4], 2)
    5
    >>> findKthLargest([3,2,3,1,2,4,5,5,6], 4)
    4
    """
    if not nums: return
    pivot = random.choice(nums)
    greater =  [x for x in nums if x > pivot]
    mid  =  [x for x in nums if x == pivot]
    smaller = [x for x in nums if x < pivot]
    
    G, M = len(greater), len(mid)
    
    if k <= G:
        return findKthLargest(greater, k)
    elif k > G + M:
        return findKthLargest(smaller, k - G - M)
    else:
        return mid[0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
