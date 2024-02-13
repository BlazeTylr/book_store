# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

_In this template, we'll use an example table `students`_

```

Table: book_store

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here.

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq; -- replace with your own table name.

CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255)
);

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO books (title, author_name) VALUES ('Nineteen Eighty-Four', 'George Orwell');
INSERT INTO books (title, author_name) VALUES ('Mrs Dalloway', 'Virginia Woolf');
INSERT INTO books (title, author_name) VALUES ('Emma', 'Jane Austen');
INSERT INTO books (title, author_name) VALUES ('Dracula', 'Bram Stoker');
INSERT INTO books (title, author_name) VALUES ('The Age of Innocence', 'Edith Wharton');

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books


# Model class
# (in lib/books.py)
class BookStore:



# Repository class
# (in lib/book_store_repository.py)
class BookStoreRepository:

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class BookStore:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

_You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed._

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class BookStoreRepository():

    def __init__(self, connection):

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT * FROM books;

        # Returns an array of Books objects.

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1

"""
Books constructs with an id, title and author_name
"""
def test_artist_constructs():
    book = BookStore(1, "Test Book", "Test Author")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author_name == "Test Author"

# 2

"""
We can format books to strings nicely
"""
def test_artists_format_nicely():
    book = BookStore(1, "Test Book", "Test Author")
    assert str(book) == "Book(1, Test Book, Test Author)"

# 3

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    book = BookStore(1, "Test Book", "Test Author")
    book_2 = BookStore(1, "Test Book", "Test Author")
    assert book == book_2

# 4
def test_get_all_records(db_connection):
    db_connection.seed('seed/book_store.sql')

    repository = BookStoreRepository(db_connection)

    books = repository.all()

    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell')
        Book(2,	'Mrs Dalloway', 'Virginia Woolf')
        Book(3, 'Emma',	'Jane Austen')
        Book(4,	'Dracula', 'Bram Stoker')
        Book(5,	'The Age of Innocence',	'Edith Wharton')
    ]

    assert len(books) == 5

```
