import time, threading

def thread_ablauf():
    global counter
    id = threading.get_ident()
    for i in range(5):
        counter += 1
        print(i, id, counter)
        time.sleep(1.5)
    return

id = threading.get_ident()
counter = 0
print(id, counter)

t1 = threading.Thread(target=thread_ablauf)
t1.start()
time.sleep(0.5)
t2 = threading.Thread(target=thread_ablauf)
t2.start()
time.sleep(10)

counter += 1
print(id, counter)
