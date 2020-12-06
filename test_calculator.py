import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
  def test_dodawanie(self):
    r = calculate(1, 2, '+')
    self.assertEqual(r, 3)

  def test_odejmowanie(self):
    r = calculate(3, 1, '-')
    self.assertEqual(r,2)
  
  def test_mnozenie(self):
    r = calculate(3, 4, '*')
    self.assertEqual(r,12)  
  
  def test_dzielenie(self):
    r = calculate(1, 3, '/')
    self.assertEqual(r,0.3333333333333333)

  def test_potegowanie(self):
    r = calculate(3, 2, '**')
    self.assertEqual(r,9)
