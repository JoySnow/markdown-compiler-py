from sentence_visitor import SentenceVisitor

class ParagraphVisitor(object):

    def __init__(self):
        self._sentence_visitor = SentenceVisitor()

    def visit(self, paragraph_node):
        ret = []
        for s in paragraph_node.sentences:
            ret.append(self._sentence_visitor.visit(s))
        return "<p>" + ''.join(ret) + "</p>"
