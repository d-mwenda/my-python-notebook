"""
Takes an object and returns a string containing a printable representation of an object,
but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes.
Syntax: ascii(object)
"""
# Todo: Revisit this concept in depth

if __name__ == "__main__":
    print(ascii('¥'))
