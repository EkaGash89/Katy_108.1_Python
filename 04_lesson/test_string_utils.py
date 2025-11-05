import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("  hello world", "hello world"),
    ("  python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symvol, expected", [
    ("skypro", "s", True),
    ("hello world","hello", True),
    ("python","a", False),
])
def test_contains_positive(input_str, symvol, expected):
    assert string_utils.contains(input_str, symvol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symvol, expected", [
    ("","s", False),
    ("skypro","S", False),
    ("   ","", True),
])   
def test_contains_negative(input_str, symvol, expected):
    assert string_utils.contains(input_str, symvol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symvol, expected", [
    ("skypro", "s", "kypro" ),
    ("hello world","hello", " world"),
    ("hello world","o", "hell wrld"),
])
def test_delete_symbol_positive(input_str, symvol, expected):
    assert string_utils.delete_symbol(input_str, symvol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symvol, expected", [
    ("python","a","python" ),
    ("skypro","S", "skypro"),
    ("   ","", "   "),
])   
def test_delete_symbol_negative(input_str, symvol, expected):
    assert string_utils.delete_symbol(input_str, symvol) == expected