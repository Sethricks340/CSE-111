from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract_city function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    assert extract_city("78 Pine St, Avon Park, FL 33825") == "Avon Park"
    assert extract_city("10101 111th Ave SE, Minot, North Dakota 58701") == "Minot"

def test_extract_state():
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"
    assert extract_state("10101 111th Ave SE, Minot, North Dakota 58701") == "North Dakota"

def test_extract_zipcode():
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440"
    assert extract_zipcode("78 Pine St, Avon Park, FL 33825") == "33825"
    assert extract_zipcode("10101 111th Ave SE, Minot, North Dakota 58701") == "58701"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])