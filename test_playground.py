import unittest
from playground import add

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,1),0)


if __name__ == '__main__':
    unittest.main()
