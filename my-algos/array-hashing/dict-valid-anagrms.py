def isAnagram(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    
    >>> isAnagram("anagram","nagaram")
    True
    >>> isAnagram("rat", "cat")
    False
    """
    if len(s) != len(t):
            return False

    countS = {}
    countT = {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT

if __name__ == "__main__":
    import doctest
    doctest.testmod()
