from scanners import SimpleScanner, TextScanner
from tokens import eof_token

#require_relative 'scanners/simple_scanner'
#require_relative 'scanners/text_scanner'
#require_relative 'token_list'

# A tokenizer, the purpose of this class is to transform a markdown string
# into a list of "tokens". In this case, each token has a type and a value.
#
# Example:
#   "_Hi!_" => [{type: UNDERSCORE, value: '_'}, {type: TEXT, value: 'Hi!'},
#               {type: UNDERSCORE, value: '_'}]
#
TOKEN_SCANNERS = (SimpleScanner, # Recognizes simple one-char tokens like `_` and `*`
                  TextScanner)  # Recognizes everything but a simple token

class Tokenizer(object):

    def tokenize(self, plain_md):
        return self.tokens_as_array(plain_md)

    def tokens_as_array(self, plain_md):
        tokens = []
        i = 0
        while plain_md != None and i < len(plain_md):
            print "DEBUG: i = ", i
            try:
                token = self.scan_one_token(plain_md[i:])
            except Exception:
                return []
            # force return [] when meet exception
            assert token.length == 2
            i += token.length
            tokens.append(token)

        tokens.append(eof_token)
        return tokens

    def scan_one_token(self, plain_md):
        for scanner in TOKEN_SCANNERS:
            token = scanner.from_string(plain_md)
            if token:
                return token
        raise Exception("The scanners could not match the given input: " + plain_md)

# TODO: why dead loop in while ???
