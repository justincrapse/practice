# future_squirrel

import time
import concurrent.futures

from multiprocessing_practice.utils import check_website
from multiprocessing_practice.websites import WEBSITE_LIST

NUM_WORKERS = 4


start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    futures = {executor.submit(check_website, address) for address in WEBSITE_LIST}
    concurrent.futures.wait(futures)

end_time = time.time()

print(f'Time for FutureSquirrel: {end_time - start_time} seconds')
