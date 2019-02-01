from ArrayQueue import ArrayQueue

a = ArrayQueue()
a.enqueue(4)
a.enqueue(1)
a.enqueue(3)
a.enqueue(5)
a.enqueue(6)
a.enqueue(7)
print(a.first())
a.dequeue()
print(a.first())
a.dequeue()
print(a.first())
a.dequeue()
print(a.first())

