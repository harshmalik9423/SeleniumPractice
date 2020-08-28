import unittest

class Test(unittest.TestCase):
    def test_one(self):
        list = ["aaa","bbb","ccc"]
        # self.assertIn("aaa",list)     #passed
        # self.assertIn("ddd",list)     #failed
        self.assertNotIn("aa",list)


if __name__ == '__main__':
    unittest.main()
