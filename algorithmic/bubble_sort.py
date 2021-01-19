
def bubble_sort(lst: list) -> list:
    """Sorts a numerical list in ascending order by comparing two numbers at a
    time, then moving the larger one further along the list.

    Args:
        lst (list): The list to be sorted.

    Returns:
        list: The list sorted in ascending order.
    """

    has_swapped = True

    n_iters = 0

    while(has_swapped):
        # Stop iterating through list if no elements were previously swapped
        has_swapped = False

        # last two elements to compare are n-2 and n-1
        for i in range(len(lst) - n_iters - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                has_swapped = True
        n_iters += 1

        return lst


a_list = [4, 1, 3, 2]
b_list = [4, 12, 499, 2, 1, 8, 66, 94, 94]
print(bubble_sort(b_list))
