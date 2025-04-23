import requests
import logging
import os
import json

STORE = '/home/grzegorz/Projects/kibana_logstash/data/'
URL = "https://www.googleapis.com/books/v1/volumes?q=harry+potter&maxResults=40"

logger = logging.getLogger('googleapis')

def __get() -> requests.Response:
    return requests.get(URL)

def __read_books() -> list:
    response = __get()
    if response.status_code != 200:
        return []
    
    data = response.json()
    if 'items' not in data:
        return []
    
    books = []
    for item in data['items']:
        books.append(item)

    response.close()
    logger.info(f'readed {len(books)} books')
    
    return books

def __read_books_and_write(file: str):
    response = __get()
    if response.status_code != 200:
        return []
    
    data = response.json()
    if 'items' not in data:
        return []
    
    books = 0
    file = os.path.join(STORE, file)
    with open(file, 'w') as f:
        for item in data['items']:
            f.write(json.dumps(item))
            f.write('\n')
            books += 1
    
    logger.info(f'readed {books} books')
    print(f'readed {books} books')
    response.close()
    

if __name__ == "__main__":
    __read_books_and_write('googleapis_books.json')
    