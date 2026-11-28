def has_duplicate(array):
    result = set()
    for value in array:
        if value in result:
            return True 
        result.add(value)
    return False


def is_anagram(first, second):
    if len(first) != len(second):
            return False
    
    result_1 = {}
    result_2 = {}

    for character in first:
        if character not in result_1:
              result_1[character] = 1
        else:
             result_1[character] += 1

    for character in second:
        if character not in result_2:
            result_2[character] = 1
        else:
            result_2[character] += 1
    
    return result_1 == result_2

def group_anagrams(words: list):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())
