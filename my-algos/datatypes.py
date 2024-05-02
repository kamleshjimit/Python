def datatypes() -> bool:
    """
    Explore all data types in python.

    >>> datatypes()
    True
    >>> datatypes()
    True
    """
    def hashset():
        s = set()
        arr = [1,2,3]
        for x in arr:
            s.add(x)        
        if 1 not in s:
            s.add(4)        
        return 4 not in s


    def dictionary():
        dict1 = {}
        dict1[1] = ['a', 'b', 'c']
        dict1[2] = 'x'
        dict1[2] += 'y'
        print(1 in dict1)
        return dict1.values()

    return hashset()
    #dictionary() == ['a', 'b', 'c', 'xy']   

if __name__ == "__main__":
    import doctest
    doctest.testmod()
