def counting_sort(array):
    if not array:
        return []

    counts = [0] * (max(array) + 1)
    for value in array:
        counts[value] += 1

    result = []
    for value in range(len(counts)):
        for _ in range(counts[value]):
            result.append(value)

    return result


if __name__ == "__main__":
    a = [0, 5, 1, 9, 1, 4, 3, 7, 1]

    print(f"\n{'=' * 6} before {'=' * 6}")
    print(a)
    
    result = counting_sort(a)

    print(f"\n{'=' * 6} after {'=' * 6}")
    print(result, "\n")