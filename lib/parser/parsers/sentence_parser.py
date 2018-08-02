#from ..nodes import Node, NullNode
from base_parser import BaseParser
from emphasis_parser import EmphasisParser
from bold_parser import BoldParser
from text_parser import TextParser
from utils import match_first


class SentenceParser(BaseParser):

    @classmethod
    def match(self, tokens):
        return match_first(tokens, EmphasisParser, BoldParser, TextParser)
