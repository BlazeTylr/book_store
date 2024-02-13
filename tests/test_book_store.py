from lib.book_store import *

"""
Books constructs with an id, title and author_name
"""
def test_artist_constructs():
    book = BookStore(1, "Test Book", "Test Author")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author_name == "Test Author"

"""
We can format books to strings nicely
"""
def test_artists_format_nicely():
    book = BookStore(1, "Test Book", "Test Author")
    assert str(book) == "Book(1, Test Book, Test Author)"

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    book = BookStore(1, "Test Book", "Test Author")
    book_2 = BookStore(1, "Test Book", "Test Author")
    assert book == book_2