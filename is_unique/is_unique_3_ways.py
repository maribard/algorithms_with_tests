def is_unique_with_dict(string):
    assert type(string) is str, f"Type of given param ({string}) is not str"
    assert len(string) > 0, f"Length of string is 0"
    counter_of_chars = {}
    for char in string:
        if char not in counter_of_chars:
            counter_of_chars[char] = 1
        else:
            return False
    return True


def is_unique_with_bit_vector(string):
    assert type(string) is str, f"Type of given param ({string}) is not str"
    assert len(string) > 0, f"Length of string is 0"
    checker = 0

    for char in string:
        val = ord(char)

        # Sprawdza, czy dany bit jest już ustawiony w 'checker'
        if (checker & (1 << val)) > 0:
            return False

        # Ustawia dany bit na 'checker' poprzez wykonanie operacji OR
        checker |= (1 << val)
    return True


def is_unique_with_sorting(string):
    assert type(string) is str, f"Type of given param ({string}) is not str"
    assert len(string) > 0, f"Length of string is 0"
    sorted_string = sorted(string)

    for i in range(len(sorted_string)-1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    return True
