import threading
import os

def run_client():
    os.system("python client.py")

threads = []

for _ in range(2):
    t = threading.Thread(target=run_client)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
