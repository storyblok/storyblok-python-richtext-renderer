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
            'attrs': node.get('attrs')
          }
        ]
      }


def heading(node):
    level = node.get('attrs').get('level')
    return return_dict('tag', 'h{}'.format(level))


def image(node):
    return {
        'single_tag': [{
          'tag': 'img',
          'attrs': utils.pick(node.get('attrs'), ['src', 'alt', 'title'])
        }]
    }


def link(node):
    attrs = node.get('attrs')
    linktype = attrs.get('linktype', 'url')
    anchor = attrs.get('anchor', None)

    if (linktype == 'email'):
        attrs['href'] = 'mailto:' + attrs.get('href')
    
    if (anchor):
        attrs['href'] = attrs.get('href') + '#' + anchor
        del attrs['anchor']


    return {
        'tag': [{
          'tag': 'a',
          'attrs': attrs
        }]
    }


def styled(node):
    return {
        'tag': [{
          'tag': 'span',
          'attrs': node.get('attrs')
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