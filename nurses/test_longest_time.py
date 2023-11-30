import pytest
from nurses.longest_time import find_nurse_with_longest_slot

@pytest.mark.parametrize("slots, expected_result", [
    ([[0, 3], [1, 5], [2, 10]],  'c')
])
def test_longest_time_basic_scenario(slots, expected_result):
    assert find_nurse_with_longest_slot(slots) == expected_result


@pytest.mark.parametrize("slots, expected_result", [
    ([[0, 3], [1, 5], [0, 8], [2, 12]],  'c')
])
def test_longest_time_two_the_same_nurses(slots, expected_result):
    assert find_nurse_with_longest_slot(slots) == expected_result


@pytest.mark.parametrize("slots, expected_result", [
    ([[0, 3], [1, 5], [0, 7], [2, 9]],  'a')
])
def test_longest_time_two_the_same_nurses_first_slot_longest(slots, expected_result):
    assert find_nurse_with_longest_slot(slots) == expected_result


@pytest.mark.parametrize("slots, expected_result", [
    ([[0, 3], [1, 5], [0, 9], [2, 10]],  'a')
])
def test_longest_time_two_the_same_nurses_second_slot_longest(slots, expected_result):
    assert find_nurse_with_longest_slot(slots) == expected_result


@pytest.mark.parametrize("slots, expected_result", [
    ([[0, 3], [1, 5], [0, 9], [25, 13]],  'z')
])
def test_longest_time_last_nurse_id(slots, expected_result):
    assert find_nurse_with_longest_slot(slots) == expected_result


@pytest.mark.parametrize("slots, expected_result", [
    ([[1, 5]],  'b')
])
def test_longest_time_one_slot(slots, expected_result):
    assert find_nurse_with_longest_slot(slots) == expected_result

