import time, threading

def thread_ablauf():
    print("Start Neben-Thread")
    for i in range(5):
        print(i, time.time())
        time.sleep(1.5)
    print("Ende Neben-Thread")

print("Start Haupt-Thread")
t = threading.Thread(target=thread_ablauf)
t.start()
time.sleep(10)
print("Ende Haupt-Thread")
