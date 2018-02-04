# threaded_squirrel.py

import time
from queue import Queue
from threading import Thread
import multiprocessing

from multiprocessing_practice.utils import check_website
from multiprocessing_practice.websites import WEBSITE_LIST

NUM_WORKERS = 4
task_queue = Queue()


def worker():
    que_size = 1
    while que_size > 0:
        address = task_queue.get()
        check_website(address)

        task_queue.task_done()
        que_size = task_queue.qsize()


start_time = time.time()

threads = [Thread(target=worker) for _ in range(NUM_WORKERS)]
[task_queue.put(item) for item in WEBSITE_LIST]
[thread.start() for thread in threads]
task_queue.join()

end_time = time.time()

print(f'Time for ThreadedSquirrel: {end_time - start_time} seconds')
