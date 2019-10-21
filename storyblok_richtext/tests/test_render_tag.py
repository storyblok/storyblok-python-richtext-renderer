import unittest
from storyblok_richtext.utils import render_tag

class TestRenderTag(unittest.TestCase):
    def test_render_tag_without_anything(self):
        self.assertEqual(render_tag(''), '<>')

    def test_render_tag_with_string(self):
        self.assertEqual(render_tag('p'), '<p>')
    
    def test_render_tag_with_ending(self):
        self.assertEqual(render_tag('br', ' /'), '<br />')
    
    def test_render_tag_with_list_of_strings(self):
        options = [ 'p', 'br' ]
        self.assertEqual(render_tag(options), '<p><br>')
    
    def test_render_tag_with_list_of_dicts(self):
        options = [{
            'tag': 'br'
        }, {
            'tag': 'p'
        }]
        self.assertEqual(render_tag(options), '<br><p>')
    
    def test_render_tag_with_list_of_dicts_with_attrs(self):
        options = [{
            'tag': 'p',
            'attrs': {
                'class': 'is-active'
            }
        }]
        self.assertEqual(render_tag(options), '<p class="is-active">')


if __name__ == "__main__":
    unittest.main()