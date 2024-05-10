def trap(height: list[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    >>> trap([0,1,0,2,1,0,1,3,2,1,2,1])
    6
    >>> trap([4,2,0,3,2,5])
    9
    """   
    N= len(height)
    if N==0:
        return 0
    left = [0]*N
    right =[0]*N
    left[0] = height[0]
    for i in range(1, N, 1):
        left[i] = max(left[i-1], height[i])        
    right[N-1] = height[N-1]
    for i in range(N-2, -1, -1):
        right[i] = max(right[i+1], height[i])
    total = 0
    for i in range(N):
        total += min(left[i], right[i]) - height[i]
    return total
if __name__ == "__main__":
    import doctest
    doctest.testmod()
