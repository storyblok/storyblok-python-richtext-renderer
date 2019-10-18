import unittest
from storyblok_richtext.utils import render_closing_tag

class TestRenderClosingTag(unittest.TestCase):
    def test_render_with_without_argument(self):
        self.assertEqual(render_closing_tag(''), '</>')

    def test_render_paragraph(self):
        self.assertEqual(render_closing_tag('p'), '</p>')
    
    def test_render_italic(self):
        self.assertEqual(render_closing_tag('i'), '</i>')
    
    def test_render_pre(self):
        self.assertEqual(render_closing_tag('pre'), '</pre>')
    
    def test_render_with_list_of_object(self):
        options = [{ 'tag': 'p' }, { 'tag': 'pre' }]
        self.assertEqual(render_closing_tag(options), '</pre></p>')
    
    def test_render_with_list_of_string(self):
        options = ['p', 'pre']
        self.assertEqual(render_closing_tag(options), '</pre></p>')


if __name__ == "__main__":
    unittest.main()