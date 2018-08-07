from pprint import pprint
from lib.tokenizer.tokenizer import Tokenizer
from lib.parser.parser import Parser


tokenizer = Tokenizer()
parser = Parser()


def test_simple():
    markdown = "__Foo__ and *bar*.\n\nAnother para."
    tokens = tokenizer.tokenize(markdown)
    print "++test-BUG: , tokens ", tokens
    print "++test-BUG: len ", len(tokens)
    for t in tokens:
        print "++test-BUG tokens sting: ", t.to_s()
    print "++test-BUG end of tokens"

    print "++test-BUG: , self.parser, ", parser
    body_node = parser.parse(tokens)
    assert body_node.consumed == 14
    print "XXXXXXXXXXX body_node: "
    pprint(body_node.to_s())
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

