from ..nodes import Node, NullNode
from base_parser import BaseParser


class EmphasisParser(BaseParser):

    @classmethod
    def match(self, tokens):
        EMPHASIZED_TEXT = (
                ('UNDERSCORE', 'TEXT', 'UNDERSCORE'),
                ('STAR', 'TEXT', 'STAR'))

        if tokens and len(tokens) >= 3:
            tokens_type = [t.type for t in tokens[:3]]
            if tuple(tokens_type) in EMPHASIZED_TEXT:
                return Node('EMPHASIS', tokens[1].value, 3)
        return NullNode()
