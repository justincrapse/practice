import threading
import os
import time
import multiprocessing

from multiprocessing_practice.utils import check_website
from multiprocessing_practice.websites import WEBSITE_LIST

NUM_WORKERS = 8


def run_stuff():
    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        results = pool.map_async(check_website, WEBSITE_LIST)
        results.wait()


def compute_stuff():
    """ Do some computations """
    print(f'PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, '
          f'Thread Name: {threading.current_thread().name}')
    x = 0
    while x < 10000000:
        x += 1


def do_the_thing():
    processes = [multiprocessing.Process(target=compute_stuff) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]


def do_threads():
    threads = [threading.Thread(target=compute_stuff) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


if __name__ == '__main__':
    start_time = time.time()
    do_the_thing()
    end_time = time.time()
    print("Time for MultiProcessingSquirrel: %ssecs" % (end_time - start_time))

    start_time = time.time()
    do_threads()
    end_time = time.time()
    print("Time for threads................: %ssecs" % (end_time - start_time))
