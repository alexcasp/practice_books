from city_functions import get_country_city
import unittest

class test_countries(unittest.TestCase):
    def test_country(self):
        get_test_country = get_country_city('chicago', 'usa')
        self.assertEqual(get_test_country, 'Chicago, Usa')
        
if __name__ == '__main__':
    unittest.main()