from base_parser import BaseParser
from sentences_and_eof_parser import SentencesAndEofParser
from sentences_and_newline_parser import SentencesAndNewlineParser
from utils import match_first


class ParagraphParser(BaseParser):

    @classmethod
    def match(self, tokens):
        print ">>>> ParagraphParser.match"
        node = match_first(tokens, SentencesAndNewlineParser,
                           SentencesAndEofParser)
        print ">>>> returned node: ", node
        return node
