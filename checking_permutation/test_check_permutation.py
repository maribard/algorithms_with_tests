import pytest

from checking_permutation.methods import if_one_is_perm_other_using_dicts, if_one_is_perm_other_using_lists, \
    if_one_is_perm_other_using_sorting


@pytest.mark.parametrize("one_string, other_string, expected_result", [
    ("r", "r", True),
    ("r", "t", False)
])
def test_if_one_permutation_other_with_min_len(one_string, other_string, expected_result):
    assert if_one_is_perm_other_using_dicts(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_lists(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_sorting(one_string, other_string) == expected_result


@pytest.mark.parametrize("one_string, other_string, expected_result", [
    ("qwertyuiop", "poiuytrewq", True),
    ("qwertypppp", "ppppytrewq", True),
    ("qwertypppp", "ppppytrewqt", False)
])
def test_if_one_permutation_other_with_middle_len(one_string, other_string, expected_result):
    assert if_one_is_perm_other_using_dicts(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_lists(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_sorting(one_string, other_string) == expected_result


def test_if_one_permutation_other_with_max_len_with_repeating():
    one_string = "qwertyppppqwertyppppqwertyppppqwertyppppqwertyppppqwertyppppqwertyppppqwertyppppqwertyppppqwertypppp"
    other_string = "ppppytrewqqwertyppppqwertyppppqwertyppppqwertyppppppppytrewqqwertyppppqwertyppppqwertyppppqwertypppp"
    expected_result = True
    assert if_one_is_perm_other_using_dicts(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_lists(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_sorting(one_string, other_string) == expected_result


@pytest.mark.parametrize("one_string, other_string, expected_result", [
    ("", "", False),
    ("", "ppp", False),
    ("qwe", "", False)
])
def test_if_one_permutation_other_with_empty_strings(one_string, other_string, expected_result):
    assert if_one_is_perm_other_using_dicts(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_lists(one_string, other_string) == expected_result
    assert if_one_is_perm_other_using_sorting(one_string, other_string) == expected_result


@pytest.mark.parametrize("one_string, other_string, expected_result", [
    (12, "", AssertionError),
    ("", 12, AssertionError),
    (11, 12, AssertionError),
    ((), (), AssertionError),
    (True, False, AssertionError),
    (None, 12, AssertionError)
])
def test_if_one_permutation_other_with_diff_params(one_string, other_string, expected_result):
    with pytest.raises(AssertionError):
        assert if_one_is_perm_other_using_dicts(one_string, other_string)
        assert if_one_is_perm_other_using_lists(one_string, other_string)
        assert if_one_is_perm_other_using_sorting(one_string, other_string)


def test_if_one_permutation_other_with_no_params():
    with pytest.raises(TypeError):
        assert if_one_is_perm_other_using_dicts()
        assert if_one_is_perm_other_using_lists()
        assert if_one_is_perm_other_using_sorting()
