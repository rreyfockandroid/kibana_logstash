import client_book.openlib_client_book as c
import writer as w
import logging
import conf.config as conf

# pobiera tylko czesc - domyslny limit
def get_filtered_books() -> list:
    filter = lambda book: {
        'title': book.get('title'),
        'year': book.get('first_publish_year')
    }
    params = {
        'q': 'django'
    }
    return c.read_books(params, filter)

# pobiera tylko czesc - domyslny limit
def get_books():
    params = {
        'q': 'django'
    }
    return c.read_books(params)    

# pobiera wszystkie
def get_all_books():
    params = {
        'q': 'django'
    }
    return c.read_all_books(params)    

def print_boks(books: list[dict]):
    for book in books:
        print(book)



if __name__ == '__main__': 
    conf.config()  
    books = get_all_books()
    w.write_to_file_as_jsons('books_openlib_django.json', books)