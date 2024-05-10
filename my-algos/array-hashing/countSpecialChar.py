def numberOfSpecialChars(word: str) -> int: 
    """
    You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
    Return the number of special letters in word.

    >>> numberOfSpecialChars("aaAbcBC")
    3
    >>> numberOfSpecialChars("abc")
    0  
    >>> numberOfSpecialChars("abBCab")
    1
    """
    lowerSet = set()
    upperSet = set()
    for c in word:
        if c.islower():
            lowerSet.add(c)
        else:
            upperSet.add(c)

    count = 0
    for char in lowerSet:
        if char.upper() in upperSet:
            count += 1
    return count
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()