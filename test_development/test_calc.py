import unittest
import calc

class test_calc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 15)
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()
