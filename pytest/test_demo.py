import pytest

@pytest.fixture()
def setup():
    print("Once before every method")

def testMethod1(setup):
    print("This is test Method 1")

def testMethod2(setup):
    print("This is test Method 2")

def testMethod3(setup):
    print("This is test Method 3")

