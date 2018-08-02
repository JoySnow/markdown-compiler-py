"""
This simple Markdown grammar:

    Body               := Paragraph *

    Paragraph          := SentenceAndNewline
			| SentenceAndEOF

    SentenceAndNewline := Sentences + NEWLINE + NEWLINE

    SentencesAndEOF    := Sentences + NEWLINE + EOF
			| Sentences + EOF

    Sentences          := Sentence *
        # Note: in code, this grammar is included in SentencesAnd* parsers.

    Sentence           := EmphasizedText
			| BoldText
			| Text

    EmphasizedText     := UNDERSCORE BoldText UNDERSCORE

    BoldText           := UNDERSCORE UNDERSCORE TEXT UNDERSCORE UNDERSCORE
			| STAR STAR TEXT STAR STAR

    Text               := TEXT
"""

from nodes import NullNode
from parsers.parser_factory import ParserFactory

class Parser(object):

    def __init__(self):
        print "DEBUG: Init of Pasrser ++++++"
        self._parser_factory = ParserFactory()
        self._body_parser = self._parser_factory.build('body_parser')

    def parse(self, tokens):
        print "++ Parser() .parse DEBUG: len(tokens) ", len(tokens)
        if len(tokens) == 0:
            raise Exception("Empty tokens list, ERROR!")

        body_node = self._body_parser.match(tokens)
        if isinstance(body_node, NullNode):
            raise Exception("NullNode as the body_node.")
        elif len(tokens) == body_node.consumed:
            return body_node
        else:
            raise Exception("Syntax error at : %s" % tokens[body_node.consumed])
