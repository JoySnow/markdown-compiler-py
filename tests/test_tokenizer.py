from lib.tokenizer.tokenizer import Tokenizer

tokenizer = Tokenizer()

def test_simple():
    tokens = tokenizer.tokenize('Hi')
    assert len(tokens) == 2
    assert tokens[0].type == 'TEXT'
    assert tokens[0].value == 'Hi'

def test_underscore():
    tokens = tokenizer.tokenize('_Foo_')
    assert len(tokens) == 4

    assert tokens[0].type == 'UNDERSCORE'
    assert tokens[0].value == '_'

    assert tokens[1].type == 'TEXT'
    assert tokens[1].value == 'Foo'

    assert tokens[2].type == 'UNDERSCORE'
    assert tokens[2].value == '_'

    assert tokens[3].type == 'EOF'
    assert tokens[3].value == ''

def test_paragraph():
    tokens = tokenizer.tokenize("Hello, World!\nThis is a _quite_  **long** text for what we've been testing so far.\t \n And this is another para.")
    #for t in tokens:
    #    print "tokens sting: ", t.to_s()
    assert len(tokens) == 16
