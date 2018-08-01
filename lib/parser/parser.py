from parsers.parser_factory import ParserFactory

class Parser(object):

    def __init__(self):
        self._body_parser = ParserFactory.build('body_parser')

    def parse(self, tokens):
        body_node = self._body_parser.match(tokens)
        if len(tokens) == body_node.consumed:
            return body_node
        else:
            raise "Syntax error at : %s" % tokens[body_node.consumed]
