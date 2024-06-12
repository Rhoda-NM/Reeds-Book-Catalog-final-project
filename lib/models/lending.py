# lib/models/lending.py
from models.__init__ import CURSOR, CONN

class Lending:

    all={}

    def __init__(self, book, lending_date, borrower):
        self.id = None
        self.book = book
        self.lending_date = lending_date
        self.borrower_name = borrower

    def __repr__(self):
        return f"<Lending {self.id}: {self.book}: {self.lending_date}: {self.borrower_name}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Lending instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS lendings(
                id INTEGER PRIMARY KEY,
                book TEXT,
                lending_date DATE,
                borrower_name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Lending instances"""
        sql = """
            DROP TABLE IF EXISTS lendings
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name values of the current Lending instance. Update object id attribute with the primary key value of the new row"""
        sql = """
            INSERT INTO lendings (book, lending_date, borrower_name)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.book, self.lending_date, self.borrower_name))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, book, date, borrower):
        """Initialize a new Author instance and save the object to the database"""
        lent_book = cls(book, date, borrower)
        lent_book.save()
        return lent_book
    @classmethod
    def instance_from_db(cls, row):
        """Return a book object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        borrowed_book = cls.all.get(row[0])
        if borrowed_book:
            # ensure attributes match row values in case local instance was modified
            borrowed_book.title = row[1]
            borrowed_book.lending_date = row[2]
            borrowed_book.borrower_name = row[3]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            borrowed_book = cls(row[1], row[2], row[3])
            borrowed_book.id = row[0]
            cls.all[borrowed_book.id] = borrowed_book
        return borrowed_book
    
    @classmethod
    def find_by_title(cls, title):
        """Returns Lending object corresponding to first table row matching given title"""
        sql = """
            SELECT *
            FROM lendings
            WHERE title is ?
        """
        row = CURSOR.execute(sql, (title, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def borrowed_books(cls):
        """Return a list containing a Lending object per row in the table"""
        sql = """
            SELECT *
            FROM lendings
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    def return_book(self):
        """Delete the table row corresponding to the current lent book instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM lendings
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None