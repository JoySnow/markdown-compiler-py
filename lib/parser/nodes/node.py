class NullNode(object):
    pass


null_node = NullNode()


class Node(object):

    def __init__(self, nt, v, consumed):
        self.type = nt
        self.value = v
        self.consumed = consumed


class ParagraphNode(object):

    def __init__(self, sentences, consumed):
        self.sentences = sentences
        self.consumed = consumed


class BodyNode(object):

    def __init__(self, paragraphs, consumed):
        self.paragraphs = paragraphs
        self.consumed = consumed

