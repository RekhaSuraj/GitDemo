# Any Pytest file should start with test_ or end with _test
# Pytest method names should start with test
# Any code should be wrapped in a method only
# Method name should make sense
# -k stands for method name execution, -s logs in output, -v stands for more info like metadata
# We can run specific file py.test<filename>
# We can mark(tag) tests with @pytest.mark.smoke and then run with -m
# @pytest.mark.xfail to just run the test case but not to report anything
# Fixtures are used for setup and tear down methods for test cases. conftest file to generalize fixture and make it
# available to all test cases
# Datadriven and parameterization can be done with return statements in tuple format
# When we define fixture scope to class only, then it will run once before class is initiated and once at the end
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_GreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
