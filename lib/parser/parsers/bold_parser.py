from ..nodes import Node, NullNode
from baseparse import BaseParser


class BoldParser(BaseParser):

    @classmethod
    def match(self, tokens):
        BOLD_TEXT = (
                ('UNDERSCORE', 'UNDERSCORE', 'TEXT', 'UNDERSCORE', 'UNDERSCORE'),
                ('STAR', 'STAR', 'TEXT', 'STAR', 'STAR'))

        if tokens and len(tokens) >= 5:
            tokens_type = [t.type for t in tokens[:5]]
            if tuple(tokens_type) in BOLD_TEXT:
                return Node('BOLD', tokens[2].value, 5)
        return NullNode()
