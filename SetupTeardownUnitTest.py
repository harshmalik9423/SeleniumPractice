import unittest

def setUpModule():
    print("SetUpModule called")

def tearDownModule():
    print("tearDownModule called")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):
        print("Open Application")

    @classmethod
    def tearDownClass(cls):
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advanceSearch(self):
        print("This is advance search")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge")

if __name__ == "__main__":
    unittest.main()