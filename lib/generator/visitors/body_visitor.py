from paragraph_visitor import ParagraphVisitor

class BodyVisitor(object):

    def __init__(self):
        self._paragraph_visitor = ParagraphVisitor()

    def visit(self, body_node):
        ret = []
        for p in body_node.paragraphs:
            ret.append(self._paragraph_visitor.visit(p))
        return ''.join(ret)
