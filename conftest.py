import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile being created")
    return ["Rekha", "Suraj", "rekhakirani@gmail.com"]

@pytest.fixture(params=[("chrome","Rekha","Suraj"), ("Firefox","Suraj"), ("IE", "Kirani")])
#@pytest.fixture(params=["chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param


