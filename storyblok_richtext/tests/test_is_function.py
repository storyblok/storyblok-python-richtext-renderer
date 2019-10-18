import unittest
from storyblok_richtext.utils import is_function

class TestIsFunction(unittest.TestCase):
    def test_is_function_with_lambda(self):
        self.assertTrue(is_function(lambda x : x + 1))

    def test_is_function_with_def_function(self):
        def sum_fn(a, b):
            return a + b

        self.assertTrue(is_function(sum_fn))


if __name__ == "__main__":
    unittest.main()