def maximalSquare(matrix: list[list[str]]) -> int:
    """
    Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
    >>> maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    4
    >>> maximalSquare([["0","1"],["1","0"]])
    1
    """
    ROWS = len(matrix)
    COLS = len(matrix[0])
    Cache= {}  # (r,c) => max square length
    def helper(r, c):
        if r >= ROWS or c >= COLS:
            return 0            
        if (r,c) not in Cache:
            right = helper(r+1, c)
            bottom = helper(r, c+1)
            diagonal = helper(r+1, c+1)
                            
            Cache[(r,c)] = 0
            if matrix[r][c] == "1" :
                Cache[(r,c)] = 1 + min(right, bottom, diagonal)

        return Cache[(r,c)]
    helper(0,0)
    return max(Cache.values()) ** 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
