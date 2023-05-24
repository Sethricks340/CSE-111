from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Seth", "Ricks") == "Ricks; Seth"
    assert make_full_name("Izzy", "Moomey") == "Moomey; Izzy"
    assert make_full_name("Alexander-Benjamin", "Walker-Rozo") == "Walker-Rozo; Alexander-Benjamin"


def test_extract_family_name():
    assert extract_family_name("Moomey; Izzy") == "Moomey"
    assert extract_family_name("Ricks; Seth") == "Ricks"
    assert extract_family_name("Walker-Rozo; Alexander-Benjamin") == "Walker-Rozo"

def test_extract_given_name():
    assert extract_given_name("Moomey; Izzy") == "Izzy"
    assert extract_given_name("Ricks; Seth") == "Seth"
    assert extract_given_name("Walker-Rozo; Alexander-Benjamin") == "Alexander-Benjamin"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
