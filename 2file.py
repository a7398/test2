import time
import threading

def task():
    time.sleep(1)

# Последовательное выполнение    
start = time.time()
for _ in range(5):
    task()
print("Последовательно:", time.time() - start)

# Параллельное выполнение
start = time.time()
threads = [threading.Thread(target=task) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print("Параллельно:", time.time() - start)