from ..nodes import NullNode, ParagraphNode
from base_parser import BaseParser
from sentence_parser import SentenceParser
from utils import match_star

class SentencesAndNewlineParser(BaseParser):

    @classmethod
    def match(self, tokens):

        nodes, consumed = match_star(tokens, SentenceParser)
        if not nodes:
            return NullNode()

        if (len(tokens) > consumed + 1 and
                tokens[consumed].type == 'NEWLINE' and
                tokens[consumed+1].type == 'NEWLINE'):
            consumed += 2
            return ParagraphNode(nodes, consumed)
        else:
            return NullNode()

