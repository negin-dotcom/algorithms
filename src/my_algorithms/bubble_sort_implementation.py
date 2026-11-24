def bubble_sort(array):
    for i in range(len(array) - 1):
        swapped = False 
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True 
        if not swapped:
            break 
        
    return array


if __name__ == "__main__":
    a = [0, 5, 1, 9, 1, 4, 3, 7, 1]

    print(f"\n{'=' * 6} before {'=' * 6}")
    print(a)

    result = bubble_sort(a)

    print(f"\n{'=' * 6} after {'=' * 6}")
    print(result, "\n")