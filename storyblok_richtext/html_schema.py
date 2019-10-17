from . import utils


def return_dict(key, tag):
    return {
        key: tag
    }


def code_block(node):
    return {
        'tag': [
          'pre',
          {
            'tag': 'code',
            'attrs': node.attrs
          }
        ]
      }


def heading(node):
    level = node.attrs.level
    return return_dict('single_tag', 'h{}'.format(level))


def image(node):
    return {
        'singleTag': [{
          tag: 'img',
          attrs: utils.pick(node.attrs, ['src', 'alt', 'title'])
        }]
    }


def link(node):
    return {
        'tag': [{
          'tag': 'a',
          'attrs': node.attrs
        }]
    }


def styled(node):
    return {
        'tag': [{
          'tag': 'span',
          'attrs': node.attrs
        }]
    }


nodes = {
    'horizontal_rule': lambda x : return_dict('single_tag', 'hr'),
    'blockquote': lambda x : return_dict('tag', 'blockquote'),
    'bullet_list': lambda x : return_dict('tag', 'ul'),
    'code_block': code_block,
    'hard_break': lambda x : return_dict('single_tag', 'br'),
    'heading': heading,
    'image': image,
    'list_item': lambda x : return_dict('tag', 'li'),
    'ordered_list': lambda x : return_dict('tag', 'ol'),
    'paragraph': lambda x : return_dict('tag', 'p')
}


marks = {
    'bold': lambda x : return_dict('tag', 'b'),
    'strike': lambda x : return_dict('tag', 'strike'),
    'underline': lambda x : return_dict('tag', 'u'),
    'strong': lambda x : return_dict('tag', 'strong'),
    'code': lambda x : return_dict('tag', 'code'),
    'italic': lambda x : return_dict('tag', 'i'),
    'link': link,
    'styled': styled
}