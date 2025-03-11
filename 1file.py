import time
import threading

def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)
threads = [threading.Thread(target=get_thread, args=(f"Thread-{i}",)) for i in range(1, 6)]
for t in threads: 
	t.start()	
