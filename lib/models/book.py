# lib/models/book.py
from models.__init__ import CURSOR, CONN

class Book:

    all={}

    def __init__(self, title, author, genre, publication_yr, status= "Unread"):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_yr = publication_yr
        self.reading_status = status

    def __repr__(self):
        return f"<Book {self.id}: {self.title}: {self.author}: {self.genre}: {self.publication_yr}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Book instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author_id INTEGER,
                genre_id INTEGER
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
            INSERT INTO books (title, author_id, genre_id, publication_yr, reading_status)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.author.id, self.genre.id, self.publication_yr, self.reading_status))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, author, genre, publication_yr, reading_status):
        book = cls(title, author, genre, publication_yr, reading_status)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a book object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        book = cls.all.get(row[0])
        if book:
            # ensure attributes match row values in case local instance was modified
            book.title = row[1]
            book.author = row[2]
            book.genre = row[3]
            book.publication_yr = row[4]
            book.reading_status = row[5]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            book = cls(row[1], row[2], row[3], row[4], row[5])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        """Return a list containing a Book object per row in the table"""
        sql = """
            SELECT *
            FROM books
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