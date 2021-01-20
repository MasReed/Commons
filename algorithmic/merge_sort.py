
def merge_sort(lst: list) -> list:
    """Sorts a numerical list with a merge sort algorithm.
    Args:
        lst (list): The list to be sorted.
    Returns:
        list: The sorted list in ascending order.
    """

    if len(lst) > 1:
        # Divide into sublists
        midpoint = len(lst) // 2
        left = lst[:midpoint]
        right = lst[midpoint:]

        # Conquer each sublist
        merge_sort(left)
        merge_sort(right)

        # Sort sublist
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Check for leftover elements (when len(left) != len(right))
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return lst


if __name__ == '__main__':

    user_str = input("Enter a numerical list to sort. E.g. [12, 2.2, 43, 9, 9.]\n")
    user_str = user_str.strip('[').strip(']').split(',')
    user_list = [float(s) for s in user_str]
    print(merge_sort(user_list))
