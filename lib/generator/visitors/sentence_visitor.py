from bold_visitor import BoldVisitor
from emphasis_visitor import EmphasisVisitor
from text_visitor import TextVisitor

SENTENCE_VISITORS = {
    "BOLD": BoldVisitor,
    "EMPHASIS": EmphasisVisitor,
    "TEXT": TextVisitor,
}

class SentenceVisitor(object):

    def visit(self,node):
        try:
            visitor_cls = SENTENCE_VISITORS.get(node.type)
            visitor = visitor_cls()
        except:
            raise Exception('Invalid sentence node type.')
        return visitor.visit(node)
