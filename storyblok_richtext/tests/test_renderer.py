import unittest
from storyblok_richtext import Richtext

resolver = Richtext()

class TestRichtext(unittest.TestCase):
    def test_render_span_with_class_attribute(self):
        data = {
            'type': 'doc',
            'content': [{
                'text': 'red text',
                'type': 'text',
                'marks': [{
                    'type': 'styled',
                    'attrs': {
                        'class': 'red'
                    }
                }]
            }]
        }

        expected = '<span class="red">red text</span>'

        self.assertEqual(resolver.render(data), expected)
    
    def test_render_hr_tag(self):
        data = {
            'type': 'doc',
            'content': [{
                'type': 'horizontal_rule'
            }]
        }

        expected = '<hr />'

        self.assertEqual(resolver.render(data), expected)
    
    def test_render_image_tag(self):
        data = {
            'type': 'doc',
            'content': [{
                'type': 'image',
                'attrs': {
                    'src': 'https://asset',
                    'alt': 'Any description'
                }
            }]
        }

        expected = '<img src="https://asset" alt="Any description" />'

        self.assertEqual(resolver.render(data), expected)
    
    def test_render_link_tag(self):
        data = {
            'type': 'doc',
            'content': [{
                'text': 'link text',
                'type': 'text',
                'marks': [{
                    'type': 'link',
                    'attrs': {
                        'href': '/link',
                        'target': '_blank',
                        'title': 'Any title'
                    }
                }]
            }]
        }

        expected = '<a href="/link" target="_blank" title="Any title">link text</a>'

        self.assertEqual(resolver.render(data), expected)
    
    def test_render_code_tag(self):
        data = {
            'type': 'doc',
            'content': [{
                'type': 'code_block',
                'content': [{
                    'text': 'code',
                    'type': 'text'
                }]
            }]
        }

        expected = '<pre><code>code</code></pre>'

        self.assertEqual(resolver.render(data), expected)

    def test_render_heading_tag(self):
        data = {
            'type': 'doc',
            'content': [{
                'type': 'heading',
                'attrs': {
                    'level': 1
                },
                'content': [{
                    'text': 'Lorem ipsum',
                    'type': 'text'
                }]
            }]
        }

        expected = '<h1>Lorem ipsum</h1>'

        self.assertEqual(resolver.render(data), expected)
    
    def test_render_complex_paragraph(self):
        data = {
            'type': 'doc',
            'content': [{
                'type': 'paragraph',
                'content': [{
                    'text': 'Lorem ',
                    'type': 'text'
                }, {
                    'text': 'ipsum',
                    'type': 'text',
                    'marks': [{
                        'type': 'strike'
                    }]
                }, {
                    'text': ' dolor sit amet, ',
                    'type': 'text'
                }, {
                    'text': 'consectetur',
                    'type': 'text',
                    'marks': [{
                        'type': 'bold'
                    }]
                }, {
                      'text': ' ',
                      'type': 'text'
                }, {
                      'text': 'adipiscing',
                      'type': 'text',
                      'marks': [
                        {
                          'type': 'underline'
                        }
                      ]
                }, {
                    'text': ' elit. Duis in ',
                    'type': 'text'
                }, {
                    'text': 'sodales',
                    'type': 'text',
                    'marks': [{
                        'type': 'code'
                    }]
                }, {
                    'text': ' metus. Sed auctor, tellus in placerat aliquet, arcu neque efficitur libero, non euismod ',
                    'type': 'text'
                }, {
                    'text': 'metus',
                    'type': 'text',
                    'marks': [{
                        'type': 'italic'
                    }]
                }, {
                    'text': ' orci eu erat',
                    'type': 'text'
                }]
            }]
        }

        expected = '<p>Lorem <strike>ipsum</strike> dolor sit amet, <b>consectetur</b> <u>adipiscing</u> elit. Duis in <code>sodales</code> metus. Sed auctor, tellus in placerat aliquet, arcu neque efficitur libero, non euismod <i>metus</i> orci eu erat</p>'

        self.assertEqual(resolver.render(data), expected)
    
    def test_render_bullet_list(self):
        data = {
            'type': 'doc',
            'content': [{
                "type": "bullet_list",
                "content": [{
                    "type": "list_item",
                    "content": [{
                        "type": "paragraph",
                        "content": [{
                            "text": "Item 1",
                            "type": "text"
                        }]
                    }]
                }, {
                    "type": "list_item",
                    "content": [ {
                        "type": "paragraph",
                        "content": [ {
                            "text": "Item 2",
                            "type": "text"
                        }]
                    }]
                }, {
                    "type": "list_item",
                    "content": [{
                        "type": "paragraph",
                        "content": [{
                            "text": "Item 3",
                            "type": "text"
                        }]
                    }]
                }]
            }]
        }

        expected = '<ul><li><p>Item 1</p></li><li><p>Item 2</p></li><li><p>Item 3</p></li></ul>'

        self.assertEqual(resolver.render(data), expected)
    
    def test_render_ordered_list(self):
        data = {
            'type': 'doc',
            'content': [{
                "type": "ordered_list",
                "content": [{
                    "type": "list_item",
                    "content": [{
                        "type": "paragraph",
                        "content": [{
                            "text": "Item 1",
                            "type": "text"
                        }]
                    }]
                }, {
                    "type": "list_item",
                    "content": [ {
                        "type": "paragraph",
                        "content": [ {
                            "text": "Item 2",
                            "type": "text"
                        }]
                    }]
                }, {
                    "type": "list_item",
                    "content": [{
                        "type": "paragraph",
                        "content": [{
                            "text": "Item 3",
                            "type": "text"
                        }]
                    }]
                }]
            }]
        }

        expected = '<ol><li><p>Item 1</p></li><li><p>Item 2</p></li><li><p>Item 3</p></li></ol>'

        self.assertEqual(resolver.render(data), expected)