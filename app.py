from lib.database_connection import DatabaseConnection
from lib.book_store_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all artists
book_store_repository = BookStoreRepository(connection)
books = book_store_repository.all()

# List them out
for book in books:
    print(book)
