# multiprocessing_squirrel.py

import time
import socket
import multiprocessing

from multiprocessing_practice.utils import check_website
from multiprocessing_practice.websites import WEBSITE_LIST

NUM_WORKERS = 8


def run_stuff():
    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        results = pool.map_async(check_website, WEBSITE_LIST)
        results.wait()


if __name__ == '__main__':
    start_time = time.time()
    run_stuff()
    end_time = time.time()
    print("Time for MultiProcessingSquirrel: %ssecs" % (end_time - start_time))