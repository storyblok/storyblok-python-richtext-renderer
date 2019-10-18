import unittest
from storyblok_richtext.utils import render_opening_tag

class TestRenderOpeningTag(unittest.TestCase):
    def test_render_with_without_argument(self):
        self.assertEqual(render_opening_tag(''), '<>')

    def test_render_paragraph(self):
        self.assertEqual(render_opening_tag('p'), '<p>')
    
    def test_render_italic(self):
        self.assertEqual(render_opening_tag('i'), '<i>')
    
    def test_render_pre(self):
        self.assertEqual(render_opening_tag('pre'), '<pre>')


if __name__ == "__main__":
    unittest.main()