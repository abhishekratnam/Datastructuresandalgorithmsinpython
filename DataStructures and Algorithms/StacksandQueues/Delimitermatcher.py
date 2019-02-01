"""A python program to match the deliiters in an expression using Array Stack as an underlying data structure"""

from ArrayStack import ArrayStack
def is_matched(expr):
    """Return true if all delimiters are properly match; false otherwise."""
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()
expr = '[(5+x)-(y+z)]'
print(is_matched(expr))