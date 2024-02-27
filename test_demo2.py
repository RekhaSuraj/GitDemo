# Any Pytest file should start with test_ or end with _test
# Pytest method names should start with test
# Any code should be wrapped in a method only
import pytest


@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings did not match"


def test_secondCreditCard():
    a = 2
    b = 5
    assert a + 3 == b, "Addition did not match"
