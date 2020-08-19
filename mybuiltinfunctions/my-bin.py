# Convert an integer number to a binary string prefixed with “0b”


if __name__ == "__main__":
    print(bin(5))
    print(bin(4))
    print(bin(3))
    print(bin(-5))
    # specify preference for '0b' prefix
    print(format(14, '#b'), format(14, 'b'))
    print(f'{14:#b}', f'{14:b}')
