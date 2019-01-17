import sys
data = []
n = int(input())
for k in range(n): # n is must fix choice
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in Bytes :{1:4d}'.format(a,b))
    data.append(None)
