from ..nodes import Node, NullNode

def match_first(tokens, *parsers):
    """
    Tries to match one parser, the order is very important here as
    they get tested first-in-first-tried.
    If a parser matched, the function returns the matched node,
    otherwise, it returns a null node.
    """
    print "-------- match_first "
    for p in parsers:
        node = p.match(tokens)
        if not isinstance(node,NullNode):
            return node
    return NullNode()


def match_star(tokens, parser):
    """
    This method tries to match a sentence as many times as possible.
    It then returns all matched nodes.
    It's the equivalent of `*`, also known as Kleene star.
    """
    matched_nodes = []
    consumed = 0

    while True:
        node = parser.match(tokens[consumed:])
        print "++ match_star DEBUG: type of node): ", type(node), node
        if isinstance(node, NullNode):
            break
        matched_nodes.append(node)
        consumed += node.consumed

    return matched_nodes, consumed

def print_tokens(tokens):
    for t in tokens:
        print t.to_s()
    print "End of print_tokens"

def print_node(node):
    if not isinstance(node, NullNode):
        print node.type, node.value
    print "^^^^^^^ end of node print "
