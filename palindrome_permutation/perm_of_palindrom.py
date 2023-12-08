import re


def permutations(head, tail=''):
    result = []

    if len(head) == 0:
        result.append(tail)
        return result

    for i in range(len(head)):
        new_tail = tail + head[i]
        new_head = head[:i] + head[i+1:]
        result.extend(permutations(new_head, new_tail))

    return result


def devide_string(string, dict_of_len_words):
    start = 0
    result = []
    for length in dict_of_len_words.values():
        word = string[start:start + length]
        result.append(word)
        start += length

    return " ".join(result)



def check_if_string_is_permutation_of_palindrome(given_string):
    list_of_words = re.findall(r"[\w']+|[.,!?;\-]", given_string)
    dict_of_len_words = {}
    for i in range(len(list_of_words)):
        dict_of_len_words[i] = len(list_of_words[i])
    list_as_str = ''.join(list_of_words).lower()

    list_of_perm = permutations(list_as_str)
    list_of_palindroms = []
    checker = False
    for perm in list_of_perm:
        if perm == perm[::-1]:
            if perm not in list_of_palindroms:
                list_of_palindroms.append(perm)

    if len(list_of_palindroms) > 0:
        for pal in range(len(list_of_palindroms)):
            list_of_palindroms[pal] = devide_string(list_of_palindroms[pal], dict_of_len_words)

        checker = True
        return f"{checker}, permutations: {list_of_palindroms}"
    return checker

print(check_if_string_is_permutation_of_palindrome("Tact Coa"))





