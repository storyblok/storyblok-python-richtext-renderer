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

    def test_render_with_custom_schema(self):
        custom = {
            'nodes': {
                'paragraph': lambda _ : { 'tag': 'p' }
            },
            'marks': {
                'strike': lambda _ : { 'tag': 'strike' }
            }
        }

        custom_object = Richtext(schema=custom)

        data = {
            'type': 'doc',
            'content': [{
                'type': 'paragraph',
                'content': [{
                    'type': 'text',
                    'text': 'some text after ',
                }, {
                    'text': 'strike text',
                    'type': 'text',
                    'marks': [{
                        'type': 'strike'
                    }]
                }]
            }]
        }

        expected = '<p>some text after <strike>strike text</strike></p>'

        self.assertEqual(custom_object.render(data), expected)
    
    def test_render_link_tag_email(self):
        data = {
            'type': 'doc',
            'content': [{
                'text': 'an email link',
                'type': 'text',
                'marks': [{
                    'type': 'link',
                    'attrs': {
                        'href': 'email@client.com',
                        'target': '_blank',
                        'linktype': 'email'
                    }
                }]
            }]
        }

        expected = '<a href="mailto:email@client.com" target="_blank" linktype="email">an email link</a>'

        self.assertEqual(resolver.render(data), expected)

    def test_render_link_tag_with_anchor(self):
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
                        'uuid': '300aeadc-c82d-4529-9484-f3f8f09cf9f5',
                        'anchor': 'anchor-text'
                    }
                }]
            }]
        }

        expected = '<a href="/link#anchor-text" target="_blank" uuid="300aeadc-c82d-4529-9484-f3f8f09cf9f5">link text</a>'

        self.assertEqual(resolver.render(data), expected)
    
    def test_complext_structure(self):
        data = {
            'type': 'doc',
            'content': [{
                'type': 'paragraph',
                'content': [{
                        'text': 'Lorem',
                        'type': 'text',
                        'marks': [{
                            'type': 'bold'
                        }]
                    }, {
                        'text': ' ipsum, ',
                        'type': 'text'
                    }, {
                        'text': 'dolor',
                        'type': 'text',
                        'marks': [{
                            'type': 'strike'
                        }]
                    }, {
                        'text': ' sit amet ',
                        'type': 'text'
                    }, {
                        'text': 'consectetur',
                        'type': 'text',
                        'marks': [{
                            'type': 'underline'
                        }]
                    }, {
                        'text': ' adipisicing elit. ',
                        'type': 'text'
                    }, {
                        'text': 'Eos architecto',
                        'type': 'text',
                        'marks': [{
                            'type': 'code'
                        }]
                    }, {
                        'text': ' asperiores temporibus ',
                        'type': 'text'
                    }, {
                        'text': 'suscipit harum ',
                        'type': 'text',
                        'marks': [{
                            'type': 'link',
                            'attrs': {
                                'href': '/test/our-service',
                                'uuid': '931e04b7-f701-4fe4-8ec0-78be0bee8809',
                                'anchor': 'anchor-text',
                                'target': '_blank',
                                'linktype': 'story'
                            }
                        }]
                    }, {
                        'text': 'ut, fugit, cumque ',
                        'type': 'text'
                    }, {
                        'text': 'molestiae ',
                        'type': 'text',
                        'marks': [{
                            'type': 'link',
                            'attrs': {
                                'href': 'asdfsdfasf',
                                'uuid': None,
                                'anchor': None,
                                'target': '_blank',
                                'linktype': 'url'
                            }
                        }]
                    }, {
                        'text': 'ratione non adipisci, ',
                        'type': 'text'
                    }, {
                        'text': 'facilis',
                        'type': 'text',
                        'marks': [{
                            'type': 'italic'
                        }]
                    }, {
                        'text': ' inventore optio dolores. Rem, perspiciatis ',
                        'type': 'text'
                    }, {
                        'text': 'deserunt!',
                        'type': 'text',
                        'marks': [{
                            'type': 'link',
                            'attrs': {
                                'href': '/home',
                                'uuid': 'fc6a453f-9aa6-4a00-a22d-49c5878f7983',
                                'anchor': None,
                                'target': '_self',
                                'linktype': 'story'
                            }
                        }]
                    }, {
                        'text': ' Esse, maiores!',
                        'type': 'text'
                    }]
            }]
        }

        expected = '<p><b>Lorem</b> ipsum, <strike>dolor</strike> sit amet <u>consectetur</u> adipisicing elit. <code>Eos architecto</code> asperiores temporibus <a href="/test/our-service#anchor-text" uuid="931e04b7-f701-4fe4-8ec0-78be0bee8809" target="_blank" linktype="story">suscipit harum </a>ut, fugit, cumque <a href="asdfsdfasf" target="_blank" linktype="url">molestiae </a>ratione non adipisci, <i>facilis</i> inventore optio dolores. Rem, perspiciatis <a href="/home" uuid="fc6a453f-9aa6-4a00-a22d-49c5878f7983" target="_self" linktype="story">deserunt!</a> Esse, maiores!</p>'

        self.assertEqual(resolver.render(data), expected)