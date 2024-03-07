def is_palindrome(data):
    """
    Returns True if `data` is a palindrome and False otherwise.
    Hint:
        slicing is your friend, use it
    Example:
        is_palindrome('aba') == True
        is_palindrome('abc') == False
    """
    for i in range(len(data)):
        if data[i] != data[-i-1]:
            return False
    return True

def lex_compare(a, b):
    """
    Lexicographically compare `a` with `b` and return the smaller string.
    Implement the comparison yourself, do not use the `<` operator for comparing strings :)

    Example:
        lex_compare('a', 'b') == 'a'
        lex_compare('ahoj', 'buvol') == 'ahoj'
        lex_compare('ahoj', 'ahojky') == 'ahoj'
        lex_compare('dum', 'automobil') == 'automobil'
    """
    min_len = min(len(a), len(b))
    for i in range(min_len):
        if a[i] != b[i]:
            if a[i] < b[i]:
                return a
            else:
                return b
    if len(a) <= len(b):
        return a
    return b

def count_successive(string):
    """
    Go through the string and for each character, count how many times it appears in succession.
    Store the character and the count in a tuple and return a list of such tuples.

    Example:
          count_successive("aaabbcccc") == [("a", 3), ("b", 2), ("c", 4)]
          count_successive("aba") == [("a", 1), ("b", 1), ("a", 1)]
    """
    if not string:
        return []
    count = 1
    prev = string[0]
    list = []
    for i in range(1,len(string)):
        if string[i] == prev:
            count += 1
        else:
            list.append((prev, count))
            prev = string[i]
            count = 1
    list.append((prev, count))
    return list

def find_positions(items):
    """
    Go through the input list of items and collect indices of each individual item.
    Return a dictionary where the key will be an item and its value will be a list of indices
    where the item was found.

    Example:
        find_positions(["hello", 1, 1, 2, "hello", 2]) == {
            2: [3, 5],
            "hello": [0, 4],
            1: [1, 2]
        }
    """
    if not items:
        return {}
    dict = {}
    pos = 0
    for i in range(1,len(items)+1):
        if items[0] in dict:
            dict[items[0]].append(pos)
        else:
            dict[items[0]] = [pos]
        pos += 1
        items.pop(0)

    return dict

def invert_dictionary(dictionary):
    """
    Invert the input dictionary. Turn keys into values and vice-versa.
    If more values would belong to the same key, return None.

    Example:
        invert_dictionary({1: 2, 3: 4}) == {2: 1, 4: 3}
        invert_dictionary({1: 2, 3: 2}) is None
    """
    inverted_dictionary = {}
    for key, value in dictionary.items():
        if value in inverted_dictionary:
            return None
        inverted_dictionary[value] = key
    return inverted_dictionary