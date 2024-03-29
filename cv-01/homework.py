def fizzbuzz(num):
    """
    Return 'Fizz' if `num` is divisible by 3, 'Buzz' if `num` is divisible by 5, 'FizzBuzz' if `num` is divisible both by 3 and 5.
    If `num` isn't divisible neither by 3 nor by 5, return `num`.
    Example:
        fizzbuzz(3) # Fizz
        fizzbuzz(5) # Buzz
        fizzbuzz(15) # FizzBuzz
        fizzbuzz(8) # 8
    """
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    return num
    pass


def fibonacci(n):
    """
    Return the `n`-th Fibonacci number (counting from 0).
    Example:
        fibonacci(0) == 0
        fibonacci(1) == 1
        fibonacci(2) == 1
        fibonacci(3) == 2
        fibonacci(4) == 3
    """
    if (n < 2):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    pass


def dot_product(a, b):
    """
    Calculate the dot product of `a` and `b`.
    Assume that `a` and `b` have same length.
    Hint:
        lookup `zip` function
    Example:
        dot_product([1, 2, 3], [0, 3, 4]) == 1*0 + 2*3 + 3*4 == 18
    """
    temp = 0
    for i, j in zip(a, b):
        temp += i * j
    return temp
    pass


def redact(data, chars):
    """
    Return `data` with all characters from `chars` replaced by the character 'x'.
    Characters are case sensitive.
    Example:
        redact("Hello world!", "lo")        # Hexxx wxrxd!
        redact("Secret message", "mse")     # Sxcrxt xxxxagx
    """
    for char in chars:
        data = data.replace(char, 'x')
    return data
    pass


def count_words(data):
    """
    Return a dictionary that maps word -> number of occurrences in `data`.
    Words are separated by spaces (' ').
    Characters are case sensitive.

    Hint:
        "hi there".split(" ") -> ["hi", "there"]

    Example:
        count_words('this car is my favourite what car is this')
        {
            'this': 2,
            'car': 2,
            'is': 2,
            'my': 1,
            'favourite': 1,
            'what': 1
        }
    """
    word_count = {}
    if (len(data) == 0):
        return word_count
    for word in data.split(' '):
        if word in word_count:
            word_count[word] = word_count[word] + 1
        word_count[word] = word_count.get(word, 1)
        word_count[word] = word_count[word]
    return word_count
    pass


def bonus_fizzbuzz(num):
    """
    Implement the `fizzbuzz` function.
    `if`, match-case and cycles are not allowed.
    """
    fizz_result = "Fizz" * (num % 3 == 0)
    buzz_result = "Buzz" * (num % 5 == 0)
    return fizz_result + buzz_result or num
    pass


def bonus_utf8(cp):
    """
    Encode `cp` (a Unicode code point) into 1-4 UTF-8 bytes - you should know this from `Základy číslicových systémů (ZDS)`.
    Example:
        bonus_utf8(0x01) == [0x01]
        bonus_utf8(0x1F601) == [0xF0, 0x9F, 0x98, 0x81]
    """
    if cp <= 0x7F:
        return [cp]
    elif cp <= 0x7FF:
        return [(cp >> 6) | 0xC0, (cp & 0x3F) | 0x80]
    elif cp <= 0xFFFF:
        return [(cp >> 12) | 0xE0, ((cp >> 6) & 0x3F) | 0x80, (cp & 0x3F) | 0x80]
    else:
        return [(cp >> 18) | 0xF0, ((cp >> 12) & 0x3F) | 0x80, ((cp >> 6) & 0x3F) | 0x80, (cp & 0x3F) | 0x80]
    pass
