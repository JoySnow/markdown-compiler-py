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
        # TODO: check oout waht node is here, and also present.
        if node:
            return node
    return NullNode
