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

#Files

def read_file(filename):
    """
    Returns content of a file as a string.

    Uses classic file access.
    """

    f = None
    lines = 'Unable to open a file: {0}'.format(filename)
    try:
        with open(filename, mode='r') as f:
            lines = f.read()
        pass
    except FileNotFoundError:
        print('File not found: {0}'.format(filename))
        pass
    finally:
        return lines


def read_file_using_with(filename):
    """
    Returns content of a file as a string.

    Uses with statement to open a file.
    """

    lines = 'Unable to open a file: {0}'.format(filename)
    try:
        pass
    except FileNotFoundError:
        pass
    finally:
        return lines


def filter_cities(filename, **kw):
    """
    Returns a list of cities that match their population specified by restrictions.
    In **kw it will be possible to set an argument:
     'gt': only cities with a population greater than the value of the argument
     'lt': only cities with a population less than the value of the argument
    It is possible to enter none, one or both parameters at once.
    If no parameter is specified, an empty list is returned.
    Use list comprehension for filtering.
    Use so-called "unpacking" to load data.

    Reimplement the function to return a generator.
    """

    cities = read_file(filename)
    filtered = cities.split('\n')
    #print(filtered)
    if 'gt' in kw:
        return [x.split(':')[0] for x in filtered if int(x.split(':')[1]) > kw['gt']]
    if 'lt' in kw:
        return [x.split(':')[0] for x in filtered if int(x.split(':')[1]) < kw['lt']]

def main():
    """
    Main function.
    This function is run at the startup of a script thanks to the cryptic if statement below.
    """

    # file reading
    filename = 'cities.txt'
    content = read_file(filename)
    print('{} file content is: {}'.format(filename, content))

    #content = read_file_using_with(filename)
    #print('{} file content using with statement is: {}'.format(filename, content))

    # filtering
    print(filter_cities(filename, gt=500000))
    print(filter_cities(filename, lt=300000))
    print(filter_cities(filename, lt=300000, gt=500000))


if __name__ == '__main__':
    main()