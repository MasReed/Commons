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

        # P(heads) = P(tails) = .5
        if random.random() <= 0.5:
            counts['heads'] += 1
        else:
            counts['tails'] += 1

    return counts


def visualize(counts: dict) -> None:
    """Displays a simple visual representation of the relative dictionary values.

    Args:
        counts (dict): Dictionary containing integers as values for the keys
        'heads' and 'tails'.

    Returns:
        None: Prints visualization to screen.
    """
    BAR_NUM = 50  # Affects display, larger takes up more screen space on output

    heads_count = counts['heads']
    tails_count = counts['tails']
    total_count = heads_count + tails_count

    # print normalized value of each key
    for key, value in counts.items():
        bars = (value / total_count)*BAR_NUM
        print(key+':', '\u258A'*round(bars), value)


if __name__ == '__main__':
    while True:
        user_flips = input('\nHow many coinflips? ')
        visualize(flip(user_flips))
