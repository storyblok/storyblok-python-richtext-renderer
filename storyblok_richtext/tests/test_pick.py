import unittest
from storyblok_richtext.utils import pick

class TestPick(unittest.TestCase):
    def test_pick_to_image(self):
        attrs = {
            'logo': 'logo',
            'src': 'favicon.ico',
            'alt': 'An favicon',
            'title': 'An favicon'
        }

        allowed = ['src', 'alt', 'title']

        result = {
            'src': 'favicon.ico',
            'alt': 'An favicon',
            'title': 'An favicon'
        }

        self.assertEqual(pick(attrs, allowed), result)
    
    def test_pick_without_object(self):
        self.assertEqual(pick({}, []), {})


if __name__ == "__main__":
    unittest.main()