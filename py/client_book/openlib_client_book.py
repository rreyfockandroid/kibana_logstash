import requests
from typing import Callable, Any
import logging
import math

logger = logging.getLogger('client_book')

URL = "https://openlibrary.org/search.json"

def __get(url: str, params: dict=None):
    return requests.get(url, params=params)


def __read_books(url: str, params: dict=None, filter_fn: Callable[[Any], Any]=None) -> list:
    response = __get(url, params=params)
    if response.status_code != 200:
        logger.error('request error ', response.status_code)
        return []
    data = response.json()
    if filter_fn == None:
        return [book for book in data['docs']]

    return [
        filter_fn(book) for book in data['docs']           
    ]

def read_books(params: dict=None, filter_fn: Callable[[Any], Any]=None) -> list:
    return __read_books(URL, params, filter_fn)

def __read_all_books(url, params) -> list:
    all_books = []
    limit = 100
    logger.info('start reading...')
    for offset in range(0, 1000000, limit):
        params['offset'] = offset
        params['limit'] = limit
        resp = __get(url, params)
        if resp.status_code != 200:
            logger.error('request error ', resp.status_code)
            break
        data = resp.json()
        if 'docs' in data and data['docs']:
            all_books.extend(data['docs'])
            logger.info(f'reading... {len(data["docs"])}')
        else:
            break
    logger.info(f'readed {len(all_books)}')
    return all_books

def read_all_books(params: dict=None) -> list:
    return __read_all_books(URL, params)


def print_books(books: list):
    for book in books:
        print('', book['title'], ' - ', book['year']) 