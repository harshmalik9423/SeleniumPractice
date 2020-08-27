import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_one(self):
        print("test one executed")

    @unittest.skip("Skipping test two")
    def test_two(self):
        print("test two executed")

    @unittest.skipIf("1==1","Skipping test three since condition is true")
    def test_three(self):
        print("Test three executed")

    def test_four(self):
        print("Test four executed")

    def test_five(self):
        print("Test five executed")

    def test_six(self):
        print("test six executed")


if __name__ == '__main__':
    unittest.main()
