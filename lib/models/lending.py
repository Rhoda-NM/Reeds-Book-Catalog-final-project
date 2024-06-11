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