import unittest
import sys
sys.path.append('../Initial_project')
from solution import calculator


class Test(unittest.TestCase):

	def test_1(self):
		n = 10
		m = 1
		li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		self.assertEqual(-5, calculator(n, m, li))


if __name__ == '__main__':
    unittest.main()