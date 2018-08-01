from ..nodes import NullNode, BodyNode
from base_parser import BaseParser
from paragraph_parser import ParagraphParser
from utils import match_star

class BodyParser(BaseParser):

    @classmethod
    def match(self, tokens):

        nodes, consumed = match_star(tokens, ParagraphParser)
        if not nodes:
            return NullNode()
        else:
            return BodyNode(nodes, consumed)
