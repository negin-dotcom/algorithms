def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array 


if __name__ == "__main__":
    a = [0, 5, 1, 9, 1, 4, 3, 7, 1]

    result = selection_sort(a)

    print(f"\n{'=' * 6} before {'=' * 6}")
    print(a)

    print(f"\n{'=' * 6} after {'=' * 6}")
    print(result, "\n")