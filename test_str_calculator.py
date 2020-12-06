import unittest

from str_calculator import str_calculate

class TestCalculator(unittest.TestCase):
  def test_concat(self):
    r = str_calculate('a', 'b', 'concat')
    self.assertEqual(r, 'ab')

