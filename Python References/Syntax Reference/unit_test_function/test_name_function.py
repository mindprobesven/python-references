import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  def test_first_last_name(self):
    formatted_name = get_formatted_name('Tim', 'Furz')
    self.assertEqual(formatted_name, 'Tim Furzz')
  
  def test_another_first_last_name(self):
    formatted_name = get_formatted_name('Tim', 'Furz')
    self.assertEqual(formatted_name, 'Tim Furz')

if __name__ == '__main__':
  unittest.main()