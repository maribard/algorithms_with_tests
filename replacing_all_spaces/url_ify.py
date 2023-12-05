def replace_all_spaces(str_with_spaces, len_of_str):
    str_in_list = list(str_with_spaces)
    print(str_in_list)
    for index in reversed(range(len_of_str)):
        if str_in_list[index] == ' ':
            tmp_index = len_of_str + 1
            for elem in reversed(str_in_list[index+1:len_of_str]):
                str_in_list[tmp_index] = elem
                tmp_index = tmp_index - 1

            len_of_str = len_of_str + 2

            str_in_list[index] = '%'
            str_in_list[index+1] = '2'
            str_in_list[index+2] = '0'

    return ''.join(str_in_list)

my_str = "Mr John Smith    "
print(replace_all_spaces(my_str, 13))







