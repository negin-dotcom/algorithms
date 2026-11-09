def merge_sort(array: list):
    if len(array) <= 1:
        return array 

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(l1: list, l2: list) -> list:
    i = j = 0

    worker_list = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            worker_list.append(l1[i])
            i += 1
        else:
            worker_list.append(l2[j])
            j += 1

    # The remaining part.
    worker_list.extend(l1[i:])
    worker_list.extend(l2[j:])

    return worker_list


if __name__ == "__main__":
    a = [0, 5, 1, 9, 1, 4, 3, 7, 1]

    result = merge_sort(a)

    print(f"\n{'=' * 6} before {'=' * 6}")
    print(a)

    print(f"\n{'=' * 6} after {'=' * 6}")
    print(result, "\n")