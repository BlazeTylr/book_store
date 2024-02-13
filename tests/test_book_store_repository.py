from lib.book_store import *
from lib.book_store_repository import *


def test_get_all_records(db_connection):
    db_connection.seed('seeds/book_store.sql')

    repository = BookStoreRepository(db_connection)

    books = repository.all()

    assert books == [
        BookStore(1, 'Nineteen Eighty-Four', 'George Orwell'),
        BookStore(2,	'Mrs Dalloway', 'Virginia Woolf'),
        BookStore(3, 'Emma',	'Jane Austen'),
        BookStore(4,	'Dracula', 'Bram Stoker'),
        BookStore(5,	'The Age of Innocence',	'Edith Wharton')
    ]

    assert len(books) == 5