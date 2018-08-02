from ..nodes import Node, NullNode
from base_parser import BaseParser
from utils import print_tokens


class EmphasisParser(BaseParser):

    @classmethod
    def match(self, tokens):
        print ">>>>>> EmphasisParser match"
        EMPHASIZED_TEXT = (
                ('UNDERSCORE', 'TEXT', 'UNDERSCORE'),
                ('STAR', 'TEXT', 'STAR'))

        print ">>>>>> tokens : "
        print_tokens(tokens)

        if tokens and len(tokens) >= 3:
            tokens_type = [t.type for t in tokens[:3]]
            print ">>>>>> tokens_type: ", tokens_type
            if tuple(tokens_type) in EMPHASIZED_TEXT:
                print ">>>>>> matched EMPHASIS, ", tokens[1].value
                return Node('EMPHASIS', tokens[1].value, 3)
        return NullNode()
