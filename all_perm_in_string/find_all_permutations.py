small_string = "abbc"
big_string = "bdcbabdcbabcdbcbabcaabbcdcbabcd"


def check_if_a_is_permutation_of_b(a, second_dict):
    first_dict = get_amount_for_every_char(a)
    for key, value in first_dict.items():
        if key in second_dict and second_dict[key] == value:
            pass
        else:
            return False
    return True


def get_amount_for_every_char(given_string):
    counter_for_every_char = {}
    for char in given_string:
        if char in counter_for_every_char:
            counter_for_every_char[char] += 1
        else:
            counter_for_every_char[char] = 1
    return counter_for_every_char


def find_all_permutations_of_sstring_in_bstring(small_string, big_string):
    assert type(small_string) is str and type(big_string) is str, \
        f"Type of small string ({type(small_string)}) or big string ({type(big_string)}) is not str"

    len_of_small_string = len(small_string)
    len_of_big_string = len(big_string)
    assert len_of_small_string <= 10, f"Length of small string ({len_of_small_string}) is bigger than 10"
    assert len_of_big_string < 1000, f"Length of big string ({len_of_big_string}) should be less than 1000"

    list_of_permutation = []
    char_count_for_small_string = get_amount_for_every_char(small_string)

    for b in range(len_of_big_string):
        if b > len_of_big_string - len_of_small_string:
            return list_of_permutation
        if big_string[b] in small_string:
            sliding_windows = big_string[b:b + len_of_small_string]
            if check_if_a_is_permutation_of_b(sliding_windows, char_count_for_small_string):
                list_of_permutation.append(sliding_windows)
    return list_of_permutation
