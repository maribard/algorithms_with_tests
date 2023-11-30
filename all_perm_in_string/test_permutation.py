import pytest
from all_perm_in_string.find_all_permutations import find_all_permutations_of_sstring_in_bstring


@pytest.mark.parametrize("small_string, big_string, expected_result", [
    ("a", "adctyb", ['a']),
    ("a", "fdcabab", ['a', 'a']),
    ("a", "fdcdbaa", ['a', 'a']),
    ("a", "fdcdb", []),
    (" ", "fdcdbaa", []),
    (" ", "fdc ba a", [' ', ' ']),
    ("a ", "fd adba ", [' a', 'a '])
])
def test_find_all_permutations_min_length(small_string, big_string, expected_result):
    assert find_all_permutations_of_sstring_in_bstring(small_string, big_string) == expected_result


@pytest.mark.parametrize("small_string, big_string, expected_result", [
    ("abcc", "cdccab", ['ccab']),
    ("abcc", "fdcabcb", ['cabc']),
    ("abcc", "fdccab", ['ccab']),
    ("a ", "fd adba ", [' a', 'a ']),
    ("abcd", "bdcaab", ['bdca']),
    ("abcd", "fdcabab", ['dcab']),
    ("abcd", "fdcdab", ['cdab']),
    ("aarthnfgvj", "aarthnfgvjwwwww", ['aarthnfgvj']),
    ("aarthnfgvj", "q345aarhtnfgvj7777", ['aarhtnfgvj']),
    ("aurthnagvj", "12332843uarthnagvjua", ['uarthnagvj', 'arthnagvju', 'rthnagvjua']),
    ("aurthnfgvj", "aurthnfgvjwwwww", ['aurthnfgvj']),
    ("aurthnfgvj", "q345aurhtnfgvj7777", ['aurhtnfgvj']),
    ("aurthnfgvj", "12332843uarthnfgvjua", ['uarthnfgvj', 'arthnfgvju', 'rthnfgvjua']),
])
def test_find_all_permutations_medium_and_maxlength(small_string, big_string, expected_result):
    assert find_all_permutations_of_sstring_in_bstring(small_string, big_string) == expected_result


@pytest.mark.parametrize("small_string, big_string, expected_result", [
    ("", "cdccab", []),
    ("", "", []),
    ("fgdgfd", "", []),
    ("abcc", "cd", []),
    ("abcc", "ghghh", [])
])
def test_find_all_permutations_with_unexpexted_args(small_string, big_string, expected_result):
    assert find_all_permutations_of_sstring_in_bstring(small_string, big_string) == expected_result


@pytest.mark.parametrize("small_string, big_string, expected_result", [
    ("rrrrtyrtfgr", "rrrrtyrtfgre", AssertionError)
])
def test_find_all_permutations_with_to_long_first_arg(small_string, big_string, expected_result):
    with pytest.raises(expected_result) as exc_info:
        find_all_permutations_of_sstring_in_bstring(small_string, big_string)
    assert exc_info.value.args[0] == f"Length of small string ({len(small_string)}) is bigger than 10"


@pytest.mark.parametrize("small_string, expected_result", [
    ("rtyrtfgre", AssertionError)
])
def test_find_all_permutations_with_to_long_second_arg(small_string, create_data, expected_result):
    with pytest.raises(expected_result) as exc_info:
        find_all_permutations_of_sstring_in_bstring(small_string, create_data["long_string"])
    assert exc_info.value.args[0] == f"Length of big string ({len(create_data['long_string'])}) " \
        f"should be less than 1000"


@pytest.mark.parametrize("expected_result", [TypeError])
def test_find_all_permutations_with_no_args(expected_result):
    with pytest.raises(expected_result):
        find_all_permutations_of_sstring_in_bstring()


@pytest.mark.parametrize("one_arg, expected_result", [
    (True, TypeError),
    ([], TypeError)
])
def test_find_all_permutations_with_one_args(one_arg, expected_result):
    with pytest.raises(expected_result):
        find_all_permutations_of_sstring_in_bstring(one_arg)


@pytest.mark.parametrize("small_string, big_string, expected_result", [
    (12, 56, AssertionError),
    (True, False, AssertionError),
    ((), {}, AssertionError),
    (None, None, AssertionError)
])
def test_find_all_permutations_when_args_are_not_str(small_string, big_string, expected_result):
    with pytest.raises(expected_result):
        find_all_permutations_of_sstring_in_bstring(small_string, big_string)
