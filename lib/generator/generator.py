from visitors.body_visitor import BodyVisitor

class Generator(object):

    def __init__(self):
        self._body_visitor = BodyVisitor()

    def generate(self, ast):
        return self._body_visitor.visit(ast)
