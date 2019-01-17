#List comprehension are more efficient

squares = [k * k for k in range(1, n+1)]

#OR
squares = []
for k in range(1, n+1):
    squares.append(k*k)
