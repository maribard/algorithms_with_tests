import pytest
from is_unique.is_unique_3_ways import is_unique_with_dict, is_unique_with_bit_vector, is_unique_with_sorting

@pytest.mark.parametrize("string, expected_result", [
    ("a", True),
    ("1", True),
    ("*", True),
    (" ", True)
])
def test_is_unique_min_case(string, expected_result):
    assert is_unique_with_dict(string) == expected_result
    assert is_unique_with_bit_vector(string) == expected_result
    assert is_unique_with_sorting(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("abcdeftyui", True),
    ("Ǚ%♥♦♧", True),
    ("aacdeftyui", False),
    ("abcdfftyui", False),
    ("abcd  tyui", False),
    ("abcdeftyii", False),
    ("Ǚ%Ǚ", False)
])
def test_is_unique_midle(string, expected_result):
    assert is_unique_with_dict(string) == expected_result
    assert is_unique_with_bit_vector(string) == expected_result
    assert is_unique_with_sorting(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("abcdeftyiiabcdeftyiiabcdeftyiiabcdeftyiiabcdeftyiiabcdeftyiiabcdeftyiiabcdeftyiiabcdeftyiiabcdeftyii", False)
])
def test_is_unique_big_case(string, expected_result):
    assert is_unique_with_dict(string) == expected_result
    assert is_unique_with_bit_vector(string) == expected_result
    assert is_unique_with_sorting(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("", AssertionError),
    (77, AssertionError),
    ({}, AssertionError),
    (True, AssertionError),
    (None, AssertionError)
])
def test_is_unique_with_diff_args(string, expected_result):
    with pytest.raises(expected_result):
        is_unique_with_dict(string)
        is_unique_with_bit_vector(string)
        is_unique_with_sorting(string)


@pytest.mark.parametrize("expected_result", [
    TypeError
])
def test_is_unique_with_no_args(expected_result):
    with pytest.raises(expected_result):
        is_unique_with_dict()
        is_unique_with_bit_vector()
        is_unique_with_sorting()
