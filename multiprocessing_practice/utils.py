
# utils.py

import time
import logging
import requests

class WebsiteDownException(Exception):
    pass


def ping_website(address, timeout=20):
    try:
        response = requests.head(address, timeout=timeout)
        if response.status_code >=400:
            logging.warning(f'Website {address} returned status_code={response.status_code}')
            raise  WebsiteDownException()
    except requests.exceptions.RequestException:
        logging.warning(f'Timeout expired for website {address}')


def notify_owner(address):
    logging.info(f'Notifying the owner of {address} website')
    time.sleep(0.5)


def check_website(address):
    try:
        ping_website(address)
    except WebsiteDownException:
        notify_owner(address)

