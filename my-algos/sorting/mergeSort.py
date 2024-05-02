
def merge_sort(data):
    """
    Sorts a list of data using the merge sort algorithm.
    Args:
      data: The unsorted list of data.
    Returns:
      A new list containing the sorted data.
    >>> merge_sort([3,4,2])
    [2, 3, 4]
    >>> merge_sort([4,3,2,1])
    [1, 2, 3, 4]
    """
    if len(data) <= 1:
        return data  # Base case: list of one element is already sorted

    # Divide the list into two halves
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """Merges two sorted lists into a single sorted list.

    Args:
    left: The first sorted list.
    right: The second sorted list.

    Returns:
        A new list containing the merged and sorted data.
    """
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from either list
    merged += left[i:]
    merged += right[j:]
    return merged

if __name__ == "__main__":
    import doctest
    doctest.testmod()
