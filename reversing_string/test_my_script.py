from reversing_string.my_script import reverse_string


def test_reverse_string_with_long_and_short_words():
    given_param = "Jestem Mariusz i jest listopad"
    expected_result = "metseJ zsuiraM i jest dapotsil"
    assert reverse_string(given_param) == expected_result


def test_reverse_string_with_one_long_word():
    given_param = "Jeste"
    expected_result = "etseJ"
    assert reverse_string(given_param) == expected_result


def test_reverse_string_with_one_short_word():
    given_param = "Jest"
    expected_result = "Jest"
    assert reverse_string(given_param) == expected_result


def test_reverse_string_with_comma_after_short_word():
    given_param = "Jestem Mariusz i jest, listopad"
    expected_result = "metseJ zsuiraM i jest, dapotsil"
    assert reverse_string(given_param) == expected_result


def test_reverse_string_with_comma_after_long_word():
    given_param = "Jestem Mariusz, i jest, listopad"
    expected_result = "metseJ zsuiraM, i jest, dapotsil"
    assert reverse_string(given_param) == expected_result


def test_reverse_string_with_dash():
    given_param = "Miłość, sztuka, natura - te rzeczy mogą dostarczać wiele radości."
    expected_result = "ćśołiM, akutzs, arutan - te yzcezr mogą ćazcratsod eleiw icśodar."
    assert reverse_string(given_param) == expected_result