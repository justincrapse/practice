# serial_squirrel.py

import time

from multiprocessing_practice.utils import check_website
from multiprocessing_practice.websites import WEBSITE_LIST

start_time = time.time()

for address in WEBSITE_LIST:
    check_website(address)

end_time = time.time()

print(f'Time for SerialSqurrel: {end_time - start_time} seconds')

