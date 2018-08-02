from lib.tokenizer.tokenizer import Tokenizer
from lib.parser.parser import Parser
print Tokenizer
print Parser

class TestTokenizer(object):

    #def setup_function(self):
    #    print "RUN test setup"
    #    self.tokenizer = Tokenizer()

    def test_simple(self):
        markdown = "__Foo__ and *text*.\n\nAnother para."
        self.tokenizer = Tokenizer()
        tokens = self.tokenizer.tokenize(markdown)
        print "++test-BUG: , tokens ", tokens
        print "++test-BUG: len ", len(tokens)
        for t in tokens:
            print "++test-BUG tokens sting: ", t.to_s()
        print "++test-BUG end of tokens"

        self.parser = Parser()
        print "++test-BUG: , self.parser, ", self.parser
        body_node = self.parser.parse(tokens)
        assert body_node.consumed == 14
