"""Measuring amortized cost for appending python 's list class"""
from time import time

def computer_average(n):
    """Perform n appends to an empty list ad return average time elapsed."""

    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n #average per operation
