def check_if_one_away(first_str, second_str):
    if abs(len(first_str) - len(second_str)) in range(0, 2):
        counter = 0
        for char in first_str:
            if char in second_str:
                pass
            else:
                counter += 1
                if counter > 1:
                    return False
        return True
    else:
        return False

