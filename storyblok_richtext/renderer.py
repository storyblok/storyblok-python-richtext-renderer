import default_html_schema
import utils


class Richtext:
    nodes = {}
    marks = {}

    def __init__(self, schema):
        if schema is None:
            schema = default_html_schema

        self.nodes = schema.nodes
        self.marks = schema.marks
    
    def render_node(self, item):
        html = []

        if item.marks:
            for m in item.marks:
                mark = self.get_matching_mark(m)

                if mark:
                    html.push(utils.render_opening_tag(mark.tag))

        return ''.join(html)
    
    def get_matching_mark(self, item):
        fn = self.marks[item.type]

        if utils.is_function(fn):
            return fn(item)

        return None
    
    def get_matchin_node(self, item):
        fn = self.nodes[item.type]

        if utils.is_function(fn):
            return fn(item)

        return None
    