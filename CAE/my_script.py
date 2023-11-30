import re


def join_punctuations(seq, characters='.,!?;'):
    list_with_joined_punc = []
    for index in range(len(seq)):
        if seq[index] not in characters:
            list_with_joined_punc.append(seq[index])
        else:
            list_with_joined_punc[len(list_with_joined_punc) - 1] = list_with_joined_punc[
                                                                        len(list_with_joined_punc) - 1] \
                                                                    + seq[index]
    return list_with_joined_punc


def reverse_string(string_to_reverse):
    list_of_words_and_punctuations = re.findall(r"[\w']+|[.,!?;\-]", string_to_reverse)
    for index_of_elem in range(len(list_of_words_and_punctuations)):
        if len(list_of_words_and_punctuations[index_of_elem]) >= 5:
            reversed_word = list_of_words_and_punctuations[index_of_elem][::-1]
            list_of_words_and_punctuations[index_of_elem] = reversed_word

    with_punct = join_punctuations(list_of_words_and_punctuations)
    return ' '.join(with_punct)

