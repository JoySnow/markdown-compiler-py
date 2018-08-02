from ..nodes import Node, NullNode
from base_parser import BaseParser


class TextParser(BaseParser):

    @classmethod
    def match(self, tokens):
        print ">>>>>> TextParser match"
        if tokens and tokens[0].type == 'TEXT':
            print ">>>>>>TEXT ", tokens[0].value
            return Node('TEXT', tokens[0].value, 1)
        return NullNode()
