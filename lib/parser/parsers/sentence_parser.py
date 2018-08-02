#from ..nodes import Node, NullNode
from base_parser import BaseParser
from emphasis_parser import EmphasisParser
from bold_parser import BoldParser
from text_parser import TextParser
from utils import match_first, print_node


class SentenceParser(BaseParser):

    @classmethod
    def match(self, tokens):
        print ">>>>>>< SentenceParser match"
        node = match_first(tokens, EmphasisParser, BoldParser, TextParser)
        print ">>>>>>< matched node ", node
        print_node(node)
        return node
