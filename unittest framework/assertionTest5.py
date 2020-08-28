import unittest


class Test(unittest.TestCase):
    def test_one(self):
        # self.assertGreater(123,12)              # passed
        # self.assertGreaterEqual(123,123)        # failed
        # self.assertLess(12,45)                # passed
        self.assertLessEqual(12,1)


if __name__ == '__main__':
    unittest.main()
