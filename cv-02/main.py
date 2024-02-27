def envelope(string):
    """
    Returns input string with added leading and closing '!' character.

    Example:
      "Hello" -> "!Hello!"
    """
    return '!' + string + '!'
    pass
print(envelope('Hello'))

def use_envelope(lst):
    """
    Returns a list that contains strings that are enveloped using '!' character.
    Use envelope function to decouple the problem.
    """
    return list(map(envelope, lst))

    pass

print(use_envelope(['Hello','World']))

def super_print(*arg):
    """
    Prints string of joined strings from *arg separated by whitespace.
    On the top and bottom of the string, `-` character is print in the same length
    as the output string.

    Example:
      super_print("Hello", "World!")

      ------------
      Hello World!
      ------------
    """
    joined = ' '.join(arg)
    separator = '-' * len(joined)
    print(separator)
    print(joined)
    print(separator)
    pass
super_print("Hello", "World!")
