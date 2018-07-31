class InvalidTokenError(Exception):
    pass

class NullToken(object):

    length = 0

    def to_s(self):
        return "<type: %s, value: %s>" % (None, None)


class Token(object):


    def __init__(self, t, v):
        self.type = t
        self.value = v
        if None in (t, v):
            raise InvalidTokenError("Not a valid Token.", (t, v))

    @property
    def length(self):
        return len(self.value) if self.value else 0

    def to_s(self):
        return "<type: %s, value: %s>" % (self.type, self.value)

#    @classmethod
#    def null(cls):
#        return NullToken()
#
#    @classmethod
#    def eof(cls):
#        return Token('EOF', '')

null_token = NullToken()
eof_token = Token('EOF', '')
