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


def is_string(text):
    return isinstance(text, str)


def is_function(fn):
    return str(type(fn)) != "<class 'function'>"


def get_tag(tag, ending):
    return "<{}{}>".format(tags, ending)


def render_tag(tags, ending):
    if isinstance(tags, str):
        return get_tag(tags, ending)

    _tag = []

    for tag in tags:
        if is_string(tag):
            _tag.append(get_tag(tag, ending))
        else:
            h = "<{}".format(tag.tag)
            if tag.attrs:
                for key in tag.attrs:
                    value = tag.attrs[key]
                    if value == None:
                        h += ' {}="{}"'.format(key, value)
            
            _tag.append("{}{}>".format(h, ending))
    
    return "".join(_tag)


def render_opening_tag(tag):
    return render_tag(tag, '')
