#lib/models/author.py
from models.__init__ import CURSOR, CONN

class Author:

    all={}

    def __init__(self, name):
        self._id = None
        self.name = name

    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the author instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Author instances"""
        sql = """
            DROP TABLE IF EXISTS authors
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name values of the current Author instance. Update object id attribute with the primary key value of the new row"""
        sql = """
            INSERT INTO authors (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """Initialize a new Author instance and save the object to the database"""
        author = cls(name)
        author.save()
        return author
    
    def update(self):
        """Update the table row corresponding to the current Author instance."""
        sql = """
            UPDATE author
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Author instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM authors
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def author_instance(cls, row):

        """Returns an Author object having attributes from the authors table row"""
        author = cls.all.get(row[0])
        if author:
            author.name = row[1]
        else:
            author = cls(row[1])
            author.id = row[0]
            cls.all[author.id] = author
        return author
    
    @classmethod
    def find_by_name(cls, name):
        """Returns Author object corresponding to first ttable row matching given name"""
        sql = """
            SELECT *
            FROM authors
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.author_instance(row) if row else None
    
    def books(self):
        """Return books by the author"""
        author = self._id
        from models.book import Book
        self._books = [book for book in Book.all if book.author == author]
        return self._books