import pytest


@pytest.fixture()
def set_up():
    print("Start TEST")
    yield
    print("Finish TEST")


@pytest.fixture(scope="module")
def set_group():
    print("ENTER SYSTEM")
    yield
    print("EXIT SYSTEM")