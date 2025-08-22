import pytest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

@pytest.mark.smoke
def test_add(prework):
    assert add(2, 3) == 5
@pytest.mark.regression
def test_subtract(prework):
    assert sub(2, 3) == -1


@pytest.fixture(scope="function")
def prework():
    print("Prework function executed.")