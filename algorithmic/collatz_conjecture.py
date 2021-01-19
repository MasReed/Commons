"""
Collatz Conjecture - Start with a number n > 1. Find the number of steps it
takes to reach one using the following process: If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
"""


def brute_collatz(n: int, verbose: bool = False) -> list:
    """Create a Collatz Conjecture sequence for a given number, n.
    Args:
        n (int): The number to reach.
        verbose (boolean): Print the number of iterations and the sequence
    Returns:
        list: The sequence of numbers to reach n.
    """
    assert n > 1

    sequence = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2

        elif n % 2 == 1:
            n = 3 * n + 1

        sequence.append(int(n))

    if verbose:
        print('Iterations: ', len(sequence))
        print('Sequence: ', sequence)

    return sequence


if __name__ == '__main__':
    while True:
        n = input('Compute the Collatz Conjecture sequence to reach a number, n.\n')
        brute_collatz(int(n), verbose=True)
