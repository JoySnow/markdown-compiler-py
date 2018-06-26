#TODO: 
#  2. use setup
#  1. fix test error

from lib import ABC
print ABC
from lib.tokenizer.tokenizer import Tokenizer

class TestTokenizer(object):

    #def setup_function(self):
    #    print "RUN test setup"
    #    self.tokenizer = Tokenizer()


    def test_simple(self):
        print "RUN test simple"
        self.tokenizer = Tokenizer()
        tokens = self.tokenizer.tokenize('Hi')
        print tokens.to_s()
        #assert tokens.first.type, 'TEXT'
        #assert tokens.first.value, 'Hi'
        assert tokens.length == 1

#    def test_underscore
#      tokens = @tokenizer.tokenize('_Foo_')
#  
#      assert_equal tokens.first.type, 'UNDERSCORE'
#      assert_equal tokens.first.value, '_'
#  
#      assert_equal tokens.second.type, 'TEXT'
#      assert_equal tokens.second.value, 'Foo'
#  
#      assert_equal tokens.third.type, 'UNDERSCORE'
#      assert_equal tokens.third.value, '_'
#    end
#  
#    def test_paragraph
#      tokens = @tokenizer.tokenize("Hello, World!
#  This is a _quite_ **long** text for what we've been testing so far.
#  
#  And this is another para.")
#      assert_equal true, true
