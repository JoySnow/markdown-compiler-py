#TODO: 
#  2. use setup
#  1. fix test error

#from lib import ABC
from lib.tokenizer.tokenizer import Tokenizer
print Tokenizer

class TestTokenizer(object):

    #def setup_function(self):
    #    print "RUN test setup"
    #    self.tokenizer = Tokenizer()


    def test_simple(self):
        self.tokenizer = Tokenizer()
        tokens = self.tokenizer.tokenize('Hi')
        assert len(tokens) == 2
        assert tokens[0].type == 'TEXT'
        assert tokens[0].value == 'Hi'

    def test_underscore(self):
        self.tokenizer = Tokenizer()
        tokens = self.tokenizer.tokenize('_Foo_')
        assert len(tokens) == 4

        assert tokens[0].type == 'UNDERSCORE'
        assert tokens[0].value == '_'

        assert tokens[1].type == 'TEXT'
        assert tokens[1].value == 'Foo'

        assert tokens[2].type == 'UNDERSCORE'
        assert tokens[2].value == '_'

        assert tokens[3].type == 'EOF'
        assert tokens[3].value == ''

    def test_paragraph(self):
        self.tokenizer = Tokenizer()
        tokens = self.tokenizer.tokenize("Hello, World!\nThis is a _quite_  **long** text for what we've been testing so far.\t \n And this is another para.")
        #for t in tokens:
        #    print "tokens sting: ", t.to_s()
        assert len(tokens) == 16
