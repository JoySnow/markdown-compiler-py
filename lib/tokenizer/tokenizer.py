from scanners import SimpleScanner, TextScanner
from tokens import eof_token, null_token

# A tokenizer, the purpose of this class is to transform a markdown string
# into a list of "tokens". In this case, each token has a type and a value.
#
# Example:
#   "_Hi!_" => [{type: UNDERSCORE, value: '_'}, {type: TEXT, value: 'Hi!'},
#               {type: UNDERSCORE, value: '_'}]
#
TOKEN_SCANNERS = (SimpleScanner,  # Recognizes simple one-char tokens like `_` and `*`
                  TextScanner)    # Recognizes everything but a simple token


class Tokenizer(object):

    def tokenize(self, plain_md):
        return self.tokens_as_array(plain_md)

    def tokens_as_array(self, plain_md):
        tokens = []

        if plain_md:
            i = 0
            while i < len(plain_md):
                try:
                    token = self.scan_one_token(plain_md[i:])
                except Exception:
                    return []
                # force return [] when meet exception
                i += token.length
                tokens.append(token)

        tokens.append(eof_token)
        return tokens

    def scan_one_token(self, plain_md):
        for scanner in TOKEN_SCANNERS:
            token = scanner.from_string(plain_md)
            if plain_md == 'HI':
                assert token == null_token
            if token != null_token:
                return token
        raise Exception("The scanners could not match the given input: " + plain_md)
