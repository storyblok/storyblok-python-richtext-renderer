import unittest
from storyblok_richtext.utils import is_string

class TestIsString(unittest.TestCase):
    def test_is_string_with_string(self):
        self.assertTrue(is_string(''))

    def test_is_string_with_numbers(self):
        self.assertFalse(is_string(10))
    
    def test_is_string_with_string_number(self):
        self.assertTrue(is_string('10'))


if __name__ == "__main__":
    unittest.main()