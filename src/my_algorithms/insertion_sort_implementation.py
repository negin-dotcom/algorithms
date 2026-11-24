def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp 

    return array 


if __name__ == "__main__":
    a = [0, 5, 1, 9, 1, 4, 3, 7, 1]

    print(f"\n{'=' * 6} before {'=' * 6}")
    print(a)
    
    result = insertion_sort(a)

    print(f"\n{'=' * 6} after {'=' * 6}")
    print(result, "\n")