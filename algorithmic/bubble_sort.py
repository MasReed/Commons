
def bubble_sort(lst: list) -> list:
    """Sorts a numerical list in ascending order by comparing two numbers at a
    time, then moving the larger one further along the list.

    Args:
        lst (list): The list to be sorted.

    Returns:
        list: The list sorted in ascending order.
    """

    for i in range(len(lst)):
        # last two elements to compare are n-2 and n-1
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


a_list = [4, 1, 3, 2]
b_list = [4, 12, 499, 2, 1, 8, 66, 94, 94]
print(bubble_sort(b_list))
