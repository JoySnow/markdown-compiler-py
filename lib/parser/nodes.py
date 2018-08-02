class NullNode(object):
    pass


null_node = NullNode()


class Node(object):

    def __init__(self, nt, v, consumed):
        self.type = nt
        self.value = v
        self.consumed = consumed

    def to_s(self):
        return ["Node - @consumed = %s" % self.consumed,
                "@type = %s" % self.type,
                "@value = %s" % self.value,
                ]


class ParagraphNode(object):

    def __init__(self, sentences, consumed):
        self.sentences = sentences
        self.consumed = consumed

    def to_s(self):
        ret = ["ParagraphNode - @consumed = %s" % self.consumed, ]
        for s in self.sentences:
            ret.append(s.to_s())
        return ret


class BodyNode(object):

    def __init__(self, paragraphs, consumed):
        self.paragraphs = paragraphs
        self.consumed = consumed

    def to_s(self):
        ret = ["BodyNode - @consumed = %s" % self.consumed, ]
        for p in self.paragraphs:
            ret.append(p.to_s())
        return ret
