class NullNode(object):
    pass


null_node = NullNode()


class Node(object):

    def __init__(self, nt, v, consumed):
        self.type = nt
        self.value = v
        self.consumed = consumed


class ParagraphBode(object):

    def __init__(self, sentences, consumed):
        self.sentences = sentences
        self.consumed = consumed


class BodyBode(object):

    def __init__(self, paragraphs, consumed):
        self.paragraphs = paragraphs
        self.consumed = consumed

