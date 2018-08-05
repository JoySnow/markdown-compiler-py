#TODO: 
#  2. use setup
#  1. fix test error

from lib.parser.parser import Parser
from lib.tokenizer.tokenizer import Tokenizer
from lib.generator.generator import Generator

class TestGeneator(object):

    #def setup_function(self):
    #    print "RUN test setup"
    #    self.tokenizer = Tokenizer()


    def test_simple(self):
        self.tokenizer = Tokenizer()
        self.parser = Parser()
        self.generator = Generator()

        markdown = "__Foo__ and *text*.\n\nAnother para."

        tokens = self.tokenizer.tokenize(markdown)
        ast = self.parser.parse(tokens)
        html = self.generator.generate(ast)

        assert html == "<p><strong>Foo</strong> and <em>text</em>.</p><p>Another para.</p>"
