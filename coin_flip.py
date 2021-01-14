import random


def flip(n: int) -> dict:
    """Simulates `n` pseudorandom coinflips, resulting in heads or tails.

    Args:
        n (int): number of flips to simulate.

    Returns
        dict: A dictionary containing the total counts for heads or tails.
        E.g. {'heads': 50, 'tails': 50}
    """
    # initialize dictionary to hold counts for each function call
    counts = {
        'heads': 0,
        'tails': 0
    }

    # determine heads or tails for each flip of `n` flips.
    for i in range(int(n)):
        rand = random.random()

        # P(heads) = P(tails) = .5
        if rand <= 0.5:
            counts['heads'] += 1
        else:
            counts['tails'] += 1

    return counts


if __name__ == '__main__':
    while True:
        user_flips = input('How many coinflips? ')
        print(flip(user_flips))
