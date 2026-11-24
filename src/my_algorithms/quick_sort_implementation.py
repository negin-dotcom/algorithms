def quick_sort(array):
    if not array:
        return []

    
    pivot_index = -1   # last one (classic)
    pivot_value = array[pivot_index]
    counter = [0] * (max(array) + 1)
    for value in array:
        counter[value] += 1

    left_array = []
    right_array = []
    for value in array:
        if value < pivot_value:
            left_array.append(value)
        elif value > pivot_value:
            right_array.append(value)

    return (quick_sort(left_array) + 
            [pivot_value] * counter[pivot_value] + 
            quick_sort(right_array))


if __name__ == "__main__":
    a = [0, 5, 1, 9, 1, 4, 3, 7, 1]

    result = quick_sort(a)

    print(f"\n{'=' * 6} before {'=' * 6}")
    print(a)

    print(f"\n{'=' * 6} after {'=' * 6}")
    print(result, "\n")