def bad_power(x,n):
    """Compute the value x**n for integer n."""

    if n==0:
        return 1
    else:
        return x * bad_power(x, n-1)
    
def good_power(x,n):
    """Compute the value x**n for integer n."""

    if n==0:
        return 1
    else:
        partial = good_power(x, n // 2)
        result = partial *partial
        if n%2 == 1:
            result *= x
        return result
