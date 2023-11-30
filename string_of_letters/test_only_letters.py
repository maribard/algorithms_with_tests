import pytest

from string_of_letters.only_letters import check_if_lower_letters


@pytest.mark.parametrize("string, expected_result", [
    ("a", True),
    ("A", False),
    ("1", False),
    (" ", False),
    ("%", False)
])
def test_check_if_letters_with_min_len(string, expected_result):
    assert check_if_lower_letters(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("aqwertyui", True),
    ("aqwertyuI", False),
    ("Aqwertyui", False),
    ("aqwErtyui", False),
    ("aqw rtyui", False),
    ("         ", False),
    ("aqwrtyui1", False),
    ("aqw%rtyui", False)
])
def test_check_if_letters_with_max_len(string, expected_result):
    assert check_if_lower_letters(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    (456, TypeError),
    ([], TypeError),
    (None, TypeError),
    (True, TypeError),
    (False, TypeError)
])
def test_check_if_letters_with_diff_param(string, expected_result):
    with pytest.raises(expected_result):
        check_if_lower_letters(string)


@pytest.mark.parametrize("expected_result", [
    TypeError,
])
def test_check_if_letters_with_no_param(expected_result):
    with pytest.raises(expected_result):
        check_if_lower_letters()
