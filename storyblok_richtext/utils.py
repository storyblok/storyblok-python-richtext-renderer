def pick(attrs: dict, allowed: list) -> dict:
    ''' Return a dictionary with specific keys in allowed '''
    if attrs is None:
        return null

    h = {}

    for key in attrs:
        value = attrs[key]
        if (key in allowed) and (value is not None):
            h[key] = value

    return h


def is_string(text: any) -> bool:
    ''' Return if a text value is a string'''
    return isinstance(text, str)


def is_function(fn: any) -> bool:
    ''' Return if a fn value is a function '''
    return str(type(fn)) == "<class 'function'>"


def get_tag(tag, ending):
    ''' Returns a tag representation '''
    return "<{}{}>".format(tag, ending)


def get_closing_tag(tag: str) -> str:
    ''' Returns a closing tag representation '''
    return "</{}>".format(tag)


def render_tag(tags, ending = ''):
    if is_string(tags):
        return get_tag(tags, ending)

    _tag = []

    for tag in tags:
        if is_string(tag):
            _tag.append(get_tag(tag, ending))
        else:
            h = "<{}".format(tag.get('tag'))
            attrs = tag.get('attrs')
            if attrs:
                for key in attrs.keys():
                    value = attrs[key]
                    if value != None:
                        h += ' {}="{}"'.format(key, value)
            
            _tag.append("{}{}>".format(h, ending))
    
    return "".join(_tag)


def render_opening_tag(tag: str) -> str:
    ''' Returns a opening tag '''
    return render_tag(tag, '')


def render_closing_tag(tags: any) -> str:
    '''
    Returns a opening tag

    Parameters
    ----------
    tags: can be a single string, list of objects with tag field or list of strings

    Returns
    -------
    tag string 
    '''
    if is_string(tags):
        return get_closing_tag(tags)
    
    _all = []

    for tag in tags[::-1]:
        if is_string(tag):
            _all.append(get_closing_tag(tag))
        else:
            _all.append(get_closing_tag(tag.get('tag')))
    
    return "".join(_all)
