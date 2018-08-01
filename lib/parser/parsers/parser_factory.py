#from base_parser import BaseParser
from text_parser import TextParser
from bold_parser import BoldParser
from emphasis_parser import EmphasisParser
from sentence_parser import SentenceParser
from sentences_and_eof_parser import SentencesAndEofParser
from sentences_and_newline_parser import SentencesAndNewlineParser
from paragraph_parser import ParagraphParser
from body_parser import BodyParser

PARSERS = {
    'text_parser':                  TextParser,
    'bold_parser':                  BoldParser,
    'emphasis_parser':              EmphasisParser,
    'sentence_parser':              SentenceParser,
    'sentences_and_eof_parser':     SentencesAndNewlineParser,
    'sentences_and_newline_parser': SentencesAndEofParser,
    'paragraph_parser':             ParagraphParser,
    'body_parser':                  BodyParser,
}

class ParserFactory(object):

    def __init__(self):
        self._cached_parsers = {}  # store (parser_class, parser_instance) maps

    @classmethod
    def build(self, name):
        parser_class = PARSERS.get(name.lower())
        if not parser_class:
            raise "Invalid parser name: %s" % name

        print "DEBUG: tyep of parser_class: ", type(parser_class)
        print "DEBU: parser_class: ", parser_class

        return self._chached_parsers.setdefault(parser_class, parser_class())
