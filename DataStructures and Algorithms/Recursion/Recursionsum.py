def linear_sum(S,n):
    #Return the sum of the first n no of sequence S.

    if n == 0:
        return 0
    else:
        return linear_sum(S,n-1)+ S[n-1]
def binary_sum(S,start,stop):
    """Return the sum of the numbers in implicitslice S[start:stop]."""

    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S,start, mid) + binary_sum(S, mid, stop)

    
