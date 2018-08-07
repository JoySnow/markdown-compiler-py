from lib.parser.parser import Parser
from lib.tokenizer.tokenizer import Tokenizer
from lib.generator.generator import Generator

tokenizer = Tokenizer()
parser = Parser()
generator = Generator()

def test_simple():

    markdown = "__Foo__ and *text*.\n\nAnother para."

    tokens = tokenizer.tokenize(markdown)
    ast = parser.parse(tokens)
    html = generator.generate(ast)

    assert html == "<p><strong>Foo</strong> and <em>text</em>.</p><p>Another para.</p>"
