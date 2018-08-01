from ..nodes import Node, NullNode

def match_first(tokens, parsers):
    """
    Tries to match one parser, the order is very important here as
    they get tested first-in-first-tried.
    If a parser matched, the function returns the matched node,
    otherwise, it returns a null node.
    """
    for p in parsers:
        node = p.match(tokens)
        if node is not NullNode:
            return node
    return NullNode


def match_star(tokens, parser):
    """
    This method tries to match a sentence as many times as possible.
    It then returns all matched nodes.
    It's the equivalent of `*`, also known as Kleene star.
    """
    matched nodes = []
    consumed = 0

    while True:
        node = parser.match(tokens[consumed:])
        if node is NullNode:
            break
        matched_nodes.append(node)
        consumed += node.consumed

    return matched_nodes, consumed
