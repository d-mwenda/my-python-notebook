"""
Return a complex number with the value real + imag*1j or convert a string or number to a complex number.
class complex([real[, imag]])
"""

if __name__ == "__main__":
    # Passing a complex expression as a string
    print(complex('1+2j'))
    # The following call raises a value error because there's a white space around the operator
    try:
        print(complex('1 + 2j'))
    except ValueError as err:
        print("Python interpreter says: {0}".format(err))
    # Pass 2 integers
    print(complex(1, 6))
    # Pass string as 1st argument and int as the 2nd argument
    try:
        print(complex("5", 3))
    except TypeError as err:
        print("The Python interpreter says: {0}".format(err))
    # No argument passed
    print(complex())
    # zero real and non-zero imag argument passed
    print(complex(0, 7))
