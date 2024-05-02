def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    >>> groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    >>> groupAnagrams([""])
    [['']]
    >>> groupAnagrams(["a"])
    [['a']]

    """
    anagrams = {}

    for s in strs:
        sortedS = ''.join(sorted(s))
        if sortedS not in anagrams:
            anagrams[sortedS] = []
        anagrams[sortedS].append(s)

    return list(anagrams.values())

if __name__ == "__main__":
    import doctest

    doctest.testmod()
