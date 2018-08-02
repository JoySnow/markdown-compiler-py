import pprint
from lib.tokenizer.tokenizer import Tokenizer
from lib.parser.parser import Parser
print Tokenizer
print Parser

pp = pprint.PrettyPrinter(indent=4)


class TestTokenizer(object):

    #def setup_function(self):
    #    print "RUN test setup"
    #    self.tokenizer = Tokenizer()

    def test_simple(self):
        markdown = "__Foo__ and *bar*.\n\nAnother para."
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
        print "XXXXXXXXXXX body_node: "
        pp.pprint(body_node.to_s())
        print "XXXXXXXXXXX end of body_node. "
        assert body_node.to_s() == [
            'BodyNode - @consumed = 14',
              ['ParagraphNode - @consumed = 12',
                ['Node - @consumed = 5', '@type = BOLD', '@value = Foo'],
                ['Node - @consumed = 1', '@type = TEXT', '@value =  and '],
                ['Node - @consumed = 3', '@type = EMPHASIS', '@value = bar'],
                ['Node - @consumed = 1', '@type = TEXT', '@value = .']],
              ['ParagraphNode - @consumed = 2',
                ['Node - @consumed = 1', '@type = TEXT', '@value = Another para.'],
               ]
            ]

