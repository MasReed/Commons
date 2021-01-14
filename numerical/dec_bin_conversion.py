
def dec_to_bin(dec_num):
    binary = []
    quotient = dec_num

    while quotient != 0:
        #q, r = divmod(quotient, 2)
        remainder = quotient % 2
        quotient = quotient // 2
        binary.append(str(remainder))

    return ''.join(binary)


if __name__ == '__main__':
    print('Convert between decimals or binary, please make a choice:')
    print('[1]: Decimal -> Binary')
    print('[2]: Binary -> Decimal')

    conversion = input()
    if conversion == '1':
        dec = int(input('Enter the decimal number: '))
        print(dec_to_bin(dec))
    elif conversion == '2':
        pass
