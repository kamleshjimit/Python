def max_container_area(height):
    """
    Calculates the maximum area of water a container can hold given an array of heights.

    Args:
        height: A list of integers representing the heights of vertical lines.

    Returns:
        The maximum area of water the container can hold.

    >>> max_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49

    >>> max_container_area([1, 1])
    1

    >>> max_container_area([])
    0
    """

    begin = 0
    end = len(height) - 1
    most_water = 0

    while begin < end:
        current_height = min(height[begin], height[end])
        area = current_height * (end - begin)
        most_water = max(most_water, area)

        if height[begin] < height[end]:
            begin += 1
        else:
            end -= 1

    return most_water


if __name__ == "__main__":
    import doctest

    doctest.testmod()
