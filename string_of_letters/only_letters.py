def check_if_lower_letters(string):
    if type(string) is not str:
        raise TypeError
    for i in string:
        if not i.islower():
            return False
    return True


