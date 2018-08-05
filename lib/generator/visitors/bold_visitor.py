class BoldVisitor(object):

    def visit(self, node):
        return "<strong>" + node.value + "</strong>"
