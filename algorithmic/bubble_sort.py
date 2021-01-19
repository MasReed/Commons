
def bubble_sort(lst: list) -> list:
    """
    """

    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


a_list = [4, 1, 3, 2]
b_list = [4, 12, 499, 2, 1, 8, 66, 94, 94]
print(bubble_sort(b_list))
