import pytest

@pytest.yield_fixture()
def setup():
    print("Executed before method")
    yield
    print("Executed after method")

def testMethod1(setup):
    print("This is method 1")

def testMethod2(setup):
    print("This is method 2")