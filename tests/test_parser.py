from lib.tokenizer.tokenizer import Tokenizer
from lib.parser.parser import Parser
print Tokenizer
print Parser

class TestTokenizer(object):

    #def setup_function(self):
    #    print "RUN test setup"
    #    self.tokenizer = Tokenizer()

    def test_simple(self, markdown):
        self.tokenizer = Tokenizer()
        tokens = self.tokenizer.tokenize(markdown)

        self.parser = Parser()
        body_node = self.parser.parse(tokens)
        assert body_node.consumed == 14
