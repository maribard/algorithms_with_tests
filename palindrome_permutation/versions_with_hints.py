import re
from collections import Counter


def checking_if_str_is_perm_of_pal(string):
    list_of_words = re.findall(r"[\w']+|[.,!?;\-]", string)
    list_as_str = ''.join(list_of_words).lower()
    if len(list_as_str) % 2 == 0:
        char_set = set()
        for char in list_as_str:
            if char in char_set:
                char_set.remove(char)
            else:
                char_set.add(char)

        return len(char_set) == 0

    else:
        char_set = set()
        for char in list_as_str:
            if char in char_set:
                char_set.remove(char)
            else:
                char_set.add(char)

        return len(char_set) == 1


# much better
def checking_if_str_is_perm_of_pal_2(string):
    list_of_words = re.findall(r"[\w']+|[.,!?;\-]", string)
    list_as_str = ''.join(list_of_words).lower()
    counter = Counter(list_as_str)

    odd_count = sum(1 for count in counter.values() if count % 2 != 0)

    if len(list_as_str) % 2 == 0:
        return odd_count == 0
    else:
        return odd_count == 1


# reducing space
def checking_if_str_is_perm_of_pal_with_bit_vector(string):
    list_of_words = re.findall(r"[\w']+|[.,!?;\-]", string)
    list_as_str = ''.join(list_of_words).lower()
    checker = 0

    for char in list_as_str:
        val = ord(char)

        # Przełącza dany bit w 'checker' przy użyciu operacji XOR (^)
        checker ^= (1 << val)

    if len(list_as_str) % 2 == 0:
        return checker == 0
    else:
        return checker != 0
