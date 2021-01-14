
def fibonacci(n: int) -> int:
    """
    Calculate the fibonacci sequence for `n` iterations, recursively.
    0, 1, 1, 2, 3, 5, 8, 13, 21,...,

    Args:
        n (int): number of iterations to calculate

    Returns:
        int:
    """

    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


if __name__ == '__main__':

    while True:
        print('\nCalculate the fibonacci sequence for `n` iterations.')
        n = input("How many iterations to calculate?\n")

        try:
            n = int(n)
        except TypeError:
            print('Please enter a positive integer.')

        if n >= 35:
            print('Warning: This may take a lot of time. (Ctrl+C to cancel)')
            print('Calculating...')

        result = fibonacci(n)
        response = '\n{0} iterations of the Fibonaci sequence is {1}.'
        print(response.format(n, result))
