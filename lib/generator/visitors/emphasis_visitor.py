class EmphasisVisitor(object):

    def visit(self, node):
        return "<em>" + node.value + "</em>"
