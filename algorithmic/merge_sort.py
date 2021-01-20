
def merge_sort(lst: list) -> list:

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

        print('lst: ', lst)

    return lst


test_list = [2, 98, 65, 98.0, 4, 1209, 137]
print(merge_sort(test_list))
