from ..nodes import NullNode, BodyNode
from base_parser import BaseParser
from paragraph_parser import ParagraphParser
from utils import match_star

class BodyParser(BaseParser):

    @classmethod
    def match(self, tokens):
        print ">>> BodyParser.match"

        nodes, consumed = match_star(tokens, ParagraphParser)
        print ">>> returned nodes, consumed: ", nodes, consumed
        if not nodes:
            return NullNode()
        else:
            return BodyNode(nodes, consumed)
