import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'"""
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('Wolfgang', 'Amadeus', 'Mozart')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
if __name__ == '__main__':
    unittest.main()
