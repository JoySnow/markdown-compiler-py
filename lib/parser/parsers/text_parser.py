from ..nodes import Node, NullNode
from baseparse import BaseParser


class TextParser(BaseParser):

    @classmethod
    def match(self, tokens):
        if tokens and tokens[0].type == 'TEXT':
            return Node('TEXT', tokens[0].value, 1)
        return NullNode()
