def reverse(S, start, stop):
    """Reverse elements in emplicit slice S[start:stop]."""
    if start < stop - 1:
        S[start], S[stop-1] = S[stop - 1], S[start]
        reverse(S, start+1, stop - 1)

def reverse_iterative(S):
    
    """Reverse elements in S using tail recursion"""
    start,stop = 0,len(S)
    while start < stop - 1:
        S[start],S[stop-1] = S[stop - 1], S[start]
        start,stop = start+1, stop -1
