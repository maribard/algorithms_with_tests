def if_one_is_perm_other_using_dicts(first, second):
    assert type(first) is str and type(second) is str, f"First param ({type(first)}) or second ({type(second)})"
    "is not str"
    if len(first) != len(second) or len(first) == 0 or len(second) == 0:
        return False
    counter_of_char_for_first = {}
    counter_of_char_for_second = {}
    for char in first:
        if char not in counter_of_char_for_first:
            counter_of_char_for_first[char] = 1
        else:
            counter_of_char_for_first[char] += 1

    for char in second:
        if char not in counter_of_char_for_second:
            counter_of_char_for_second[char] = 1
        else:
            counter_of_char_for_second[char] += 1

    if counter_of_char_for_first == counter_of_char_for_second:
        return True
    else:
        return False


def if_one_is_perm_other_using_lists(first, second):
    if len(first) != len(second) or len(first) == 0 or len(second) == 0:
        return False
    first_list = list(first)
    second_list = list(second)
    for elem in first_list:
        if elem in second_list:
            second_list.remove(elem)
        else:
            return False
    return True


def if_one_is_perm_other_using_sorting(first, second):
    if len(first) != len(second) or len(first) == 0 or len(second) == 0:
        return False
    if sorted(first) == sorted(second):
        return True
    return False
