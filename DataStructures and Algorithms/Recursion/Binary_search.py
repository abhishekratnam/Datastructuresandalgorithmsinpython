import sys
old = sys.getrecursionlimit()
sys.setrecursionlimit(10000000)

def Binary_search( data, target, low, high):
    """Return True If element found at the indicated position of a list sequence.

        The search only considers the position from  data[low] to data[high] inclusive."""
    if low > high:
        return False
    else:
        mid = low + high // 2

        if target == data[mid]:
            return True

        elif target < data[mid]:
            #recur on the left portion of list
            return Binary_search(data, target, low, mid - 1)
        else:
            #recur on the right side of list

            return Binary_search(data, target, mid+1 , high)


"""Binary search Using tail recursion"""
def binary_search_iterative(data, target):
    """Return True on target Found"""

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low+high) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1

    return False
            


