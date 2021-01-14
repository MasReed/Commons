
def factorial(n: int) -> int:
    """Computes the factorial of n, recursively.

    Args:
        n (int): positive integer number to calculate factorial of.

    Returns:
        int: n factorial (n!)
    """

    try:
        # clean input to positive integer numbers
        n = float(n)
        if n == int(n) & int(n) >= 0:
            n = int(n)
        else:
            if n < 0:
                n = abs(n)
                print('*The absolute number has been used instead.')
            if n % 1 != 0:
                n = round(n)
                print('*The number has been rounded to the nearest whole number.')
            n = int(n)

    except (TypeError, ValueError):
        print('Please enter a positive integer value.')

    else:
        # Calculate factorial
        if n > 1:
            return n * factorial(n - 1)
        else:
            return 1


if __name__ == '__main__':
    while True:
        user_input = input('\nEnter an integer to calculate it\'s factorial: ')
        result = factorial(user_input)
        response = '\nThe calculated factorial is {0}.\n'
        print(response.format(result))
