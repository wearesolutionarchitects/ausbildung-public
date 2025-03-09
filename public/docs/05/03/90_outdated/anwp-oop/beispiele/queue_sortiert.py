import queue
x = queue.PriorityQueue()
x.put(5)
x.put(19)
x.put(-2)
x.put(12)
print("Anzahl Elemente:", x.qsize())

while not x.empty():
    print(x.get())
print("Anzahl Elemente:", x.qsize())
