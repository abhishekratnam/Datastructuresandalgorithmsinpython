def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""

    for k in range(1, len(A)):
        curr = A[k]
        j = k
        while j>0 and A[j-1] > curr:
            A[j] = A[j-1]
            j -= 1
        A[j] = curr
    return A
print(insertion_sort([234,3,4,3,45,3,3,5,32,3]))
