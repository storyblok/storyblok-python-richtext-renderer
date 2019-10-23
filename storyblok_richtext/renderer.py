import html
from . import utils, html_schema


class Richtext:
    nodes = {}
    marks = {}

    def __init__(self, schema = None):
        if schema is None:
            self.nodes = html_schema.nodes
            self.marks = html_schema.marks
            return

        self.nodes = schema.get('nodes')
        self.marks = schema.get('marks')
    
    def render(self, data):
        html_string = ''

        for node in data.get('content'):
            html_string += self.render_node(node)
        
        return html_string
    
    def render_node(self, item):
        data = []
        marks = item.get('marks')

        if marks:
            for m in marks:
                mark = self.get_matching_mark(m)

                if mark:
                    data.append(utils.render_opening_tag(mark.get('tag')))
        
        node = self.get_matching_node(item)

        if node is not None and node.get('tag'):
            data.append(utils.render_opening_tag(node.get('tag')))
        
        if item.get('content'):
            for content_item in item.get('content'):
                data.append(self.render_node(content_item))
        elif item.get('text'):
            data.append(html.escape(item.get('text')))
        elif node is not None and node.get('single_tag'):
            data.append(utils.render_tag(node.get('single_tag'), ' /'))
        elif node is not None and node.get('html'):
            data.append(node.get('html'))
        
        if node is not None and node.get('tag'):
            data.append(utils.render_closing_tag(node.get('tag')))

        if marks:
            for m in marks[::-1]:
                mark = self.get_matching_mark(m)

                if mark:
                    data.append(utils.render_closing_tag(mark.get('tag')))

        return ''.join(data)
    
    def get_matching_mark(self, item):
        _type = item.get('type')
        fn = self.marks.get(_type)

        if utils.is_function(fn):
            return fn(item)

        return None
    
    def get_matching_node(self, item):
        _type = item.get('type')
        fn = self.nodes.get(_type)

        if utils.is_function(fn):
            return fn(item)

        return None
    