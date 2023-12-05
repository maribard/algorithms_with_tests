import pytest
from replacing_all_spaces.url_ify import replace_all_spaces


@pytest.mark.parametrize("string, length, result", [
    ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
    (" Mr John Smith      ", 14, "%20Mr%20John%20Smith"),
    ("Mr  John Smith      ", 14, "Mr%20%20John%20Smith")
])
def test_replace_all_spaces(string, length, result):
    assert replace_all_spaces(string, length) == result