# lib/models/book.py
from models.__init__ import CURSOR, CONN
from models.author import Author
from models.genre import Genre

class Book:

    all={}

    def __init__(self, title, author_id,author_name, genre_id, genre_name, publication_yr, status= "Unread"):
        self.title = title
        self.author_id = author_id
        self.author_name = author_name
        self.genre_id = genre_id
        self.genre_name = genre_name
        self.publication_yr = publication_yr
        self.reading_status = status

    def __repr__(self):
        return f"<Book {self.id}: {self.title}: {self.author_name}: {self.genre_name}: {self.publication_yr}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Book instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author_id INTEGER,
                author_name TEXT,
                genre_id INTEGER,
                genre_name TEXT,
                publication_yr DATE,
                reading_status TEXT,
                FOREIGN KEY (author_id) REFERENCES author(id),
                FOREIGN KEY (genre_id) REFERENCES genre(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(self):
        """Drop the table that persists Book instances"""
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """Insert a new row with the title, author id genre id, publication yr, reading status.
        Update object id attributwe using the primary key value of the new row
        Save the book in a local dictionary using PK as the dictionary key"""
        sql = """
            INSERT INTO books (title, author_id, author_name, genre_id, genre_name, publication_yr, reading_status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.author_id, self.author_name, self.genre_id, self.genre_name, self.publication_yr, self.reading_status))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, author_name, genre_name, publication_yr, reading_status):
        author = Author.find_by_name(author_name)
        if not author:
            author = Author.create(author_name)
            if not author:
                raise Exception("Failed to create author")
    
        # Find or create genre
        genre = Genre.find_by_name(genre_name)
        if not genre:
            genre = Genre.create(genre_name)
            if not genre:
                raise Exception("Failed to create genre")
        book = cls(title, author.id, author_name,  genre.id, genre_name, publication_yr, reading_status)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a book object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.author_id = row[2]
            book.author_name = row[3]
            book.genre_id = row[4]
            book.genre_name = row[5]
            book.publication_yr = row[6]
            book.reading_status = row[7]
        else:
            book = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        """Return a list containing a Book object per row in the table"""
        sql = """
            SELECT * FROM books
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_title(cls, title):
        """Returns Book object corresponding to first table row matching given title"""
        sql = """
            SELECT *
            FROM books
            WHERE title is ?
        """
        row = CURSOR.execute(sql, (title, )).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def delete(self):
        """Delete the table row corresponding to the current Book instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None