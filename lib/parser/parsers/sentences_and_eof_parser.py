from ..nodes import NullNode, ParagraphNode
from base_parser import BaseParser
from sentence_parser import SentenceParser
from utils import match_star

class SentencesAndEofParser(BaseParser):

    @classmethod
    def match(self, tokens):

        print ">>>>> SentencesAndEofParser match"
        nodes, consumed = match_star(tokens, SentenceParser)
        print ">>>>> nodes, consumed: ", nodes, consumed
        if not nodes:
            return NullNode()

        if len(tokens) > consumed and tokens[consumed].type == 'EOF':
            consumed += 1
        elif (len(tokens) > consumed + 1 and
                tokens[consumed].type == 'EOF' and
                tokens[consumed+1].type == 'NewLINE'):
            consumed += 2
        else:
            return NullNode()

        return ParagraphNode(nodes, consumed)
