
def dec_to_bin(dec_num):
    """Converts a decimal number into a binary string.
    Args:
        dec_num (int): Decimal number to convert.
    Returns:
        str: Binary number as a string.
    """
    binary = []
    quotient = dec_num

    while quotient != 0:
        #q, r = divmod(quotient, 2)
        remainder = quotient % 2
        quotient = quotient // 2
        binary.append(str(remainder))

    return ''.join(binary)


def bin_to_dec(bin_str):
    """Converts a binary string into a decimal number.
    Args:
        bin_str (str): Binary string to convert.
    Returns:
        int: Decimal number.
    """
    decimal = 0
    bit_exponent = 0

    bin_str = list(bin_str)
    bin_reverse = bin_str[::-1]

    # Uses reverse of binary to exponentiate each term more cleanly.
    for bit in bin_reverse:
        bit = int(bit)
        if bit != 1 and bit != 0:
            raise ValueError('A binary number should be used.')
        decimal += bit * (2**bit_exponent)
        bit_exponent += 1

    return decimal


if __name__ == '__main__':
    print('Convert between decimals or binary, please make a choice:')
    print('[1]: Decimal -> Binary')
    print('[2]: Binary -> Decimal')

    conversion = input()
    if conversion == '1':
        dec = int(input('Enter the decimal number: '))
        print(dec_to_bin(dec))
    elif conversion == '2':
        bin = input('Enter the binary number: ')
        print(bin_to_dec(bin))
