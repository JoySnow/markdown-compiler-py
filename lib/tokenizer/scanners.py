
# -*- coding: utf-8 -*-

"""
All scanners must implement 'from_string' method. The method takes a plain markdown
string as input and returns a single token, using some logic to determine
whether it should match it or not. When matched, it returns a valid token.
Otherwise, it returns a "null token".
Note that a token knows when it's invalid — in this case when either the type
or the value are empty — that's the InvalidTokenError we are catching.
"""

from tokens import Token, InvalidTokenError, null_token

TOKEN_TYPES = {
  '_':  'UNDERSCORE',
  '*':  'STAR',
  '\n':  'NEWLINE',
}


class SimpleScanner(object):
    """
    This class scans for a token based on a single character. If there are no
    matches, it will return a NullToken.

    Eg: SimpleToken.from_string("_foo") => #<Token type:'UNDERSCORE', value: '_'>
        SimpleToken.from_string("foo")  => #<NullToken>
    """

    @classmethod
    def from_string(self, plain_markdown):
        char = plain_markdown[0]
        try:
            if char in TOKEN_TYPES:
                return Token(TOKEN_TYPES[char], char)
            else:
                raise InvalidTokenError("Not a valid SimpleScanner token type.")
        except InvalidTokenError:
            return null_token


class TextScanner(SimpleScanner):
    """
    A simple text scanner, it basically selects everything the simple scanner
    does not.
    """

    @classmethod
    def from_string(self, plain_markdown):
        text = []
        for char in plain_markdown:
            if SimpleScanner.from_string(char) == null_token:
                text.append(char)
            else:
                break
        if text:
            return Token('TEXT', ''.join(text))
        else:
            return null_token
